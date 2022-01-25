from collections import Counter

import cv2

from color_detection import ColorDetector
from frame_extract import get_contours
from utils import *


class RubexCubex:

    def __init__(self):
        self.faces = {}
        self.preview_state = {}
        self.face_states = {}
        self.output_order = ['white', 'orange', 'green', 'red', 'blue', 'yellow']
    
    def export_faces(self):
        return ""

    def add_face(self):
        if self.preview_state != {}:
            self.faces[self.preview_state[4]] = self.preview_state.copy()
            print("added " + self.preview_state[4] + " face")
    
    def update_preview_state(self, new_state):
        for face, value in new_state.items():
            if face not in self.face_states.keys():
                self.face_states[face] = []
            else:
                self.face_states[face].append(value)

        if len(self.face_states[0]) == 8:
            for index in self.face_states.keys():
                data = Counter(self.face_states[index])
                self.preview_state[index] = max(self.face_states[index], key=data.get)
            self.face_states = {}
    
    def print_faces(self):
        nn_array = self.get_nn_array()
        print_cube(nn_array)
        print(nn_array)
    
    def get_nn_array(self):
        final_faces = []
        for order_color in self.output_order:
            if order_color not in self.faces.keys():
                continue
            value = self.faces[order_color]
            face = []
            for color in value.values():
                face.append(color[0])
            final_faces.append(face[:4] + face[5:])
        return convert_to_nn_array(final_faces)
    
def show_webcam():
    cube = RubexCubex()
    color_detector = ColorDetector()
    in_calibration_mode = False
    calibration_colors = {}
    colors = ['green', 'red', 'blue', 'orange', 'white', 'yellow']
    calibration_counter = 0
    
    preview_points = [
        (10, 10), (30, 10), (50, 10),
        (10, 30), (30, 30), (50, 30),
        (10, 50), (30, 50), (50, 50)
    ]
    
    cam = cv2.VideoCapture(0)
    while True:
        _, image = cam.read()

        image = cv2.flip(image, 1)
        _, contours = get_contours(image)

        # switch to calibration mode
        if cv2.waitKey(1) == ord('c'): 
            in_calibration_mode = not in_calibration_mode

        # ESC to exit
        if cv2.waitKey(1) == 27: 
            cube.print_faces()
            break

        if in_calibration_mode:

            if calibration_counter == len(colors):
                in_calibration_mode = False
                color_detector.set_colors(calibration_colors)
                continue

            cv2.putText(image, "enter " + colors[calibration_counter] + " face (press 'a')", (10,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            if contours:
                # add color
                if cv2.waitKey(1) == ord('a'):
                    color_in_area = color_detector.get_dominant_color(image, contours[4])
                    calibration_colors[colors[calibration_counter]] = color_in_area
                    calibration_counter += 1
                contours = [contours[4]]
        else:
            cv2.putText(image, "add face (press 'f')", (10,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            new_state = color_detector.estimate_colors(image, contours)
            if new_state != {}:
                cube.update_preview_state(new_state)
            if cube.preview_state != {}:
                for index, point in enumerate(preview_points):
                    draw_preview_rect(image, point, color_detector.colors[cube.preview_state[index]])
            for face_color in colors:
                if face_color not in cube.faces.keys():
                    draw_saved_face(image, [], color_detector.colors, face_color)
                else:
                    draw_saved_face(image, cube.faces[face_color], color_detector.colors, face_color)
            # add face
            if cv2.waitKey(1) == ord('f'):
                cube.add_face()

        draw_bounding_rect(image, contours)
        cv2.imshow('RubexCubex', image)
    
    cv2.destroyAllWindows()

def draw_bounding_rect(image, bounding_rects):
    for bounding_rect in bounding_rects:
        (x, y, w, h) = bounding_rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)

def draw_preview_rect(image, point, color):
    (x, y) = point
    cv2.rectangle(image, (x, y), (x + 15, y + 15), convert_color_to_int(color), -1)

def convert_color_to_int(color):
    return (int(color[0]), int(color[1]), int(color[2]))

def draw_saved_face(image, face, colors, color):
    face_roots = {
        "green": (410, 300),
        "red": (480, 300),
        "blue": (550, 300),
        "orange": (340, 300),
        "white": (410, 230),
        "yellow": (410, 370),
    }
    (x, y) = face_roots[color]

    for index in range(0, 9):
        x_offset = index % 3 + 1
        y_offset = index // 3 + 1
        color =  colors[face[index]] if face != [] else (192, 192, 192)
        draw_preview_rect(image, (x + 20 * x_offset, y + 20 * y_offset), color)

def convert_to_nn_array(final_faces):
    nn_array = []
    for face in final_faces:
        for color in face:
            nn_array.extend(colours_dict[color])
    return nn_array

def main():
    show_webcam()


if __name__ == '__main__':
    main()
    # nesto = convert_to_nn_array([['o', 'w', 'o', 'g', 'b', 'w', 'w', 'g'], ['b', 'o', 'o', 'b', 'g', 'y', 'r', 'r'], ['g', 'g', 'y', 'y', 'g', 'b', 'b', 'w'], ['r', 'r', 'b', 'r', 'o', 'r', 'o', 'w'], ['y', 'r', 'w', 'w', 'w', 'b', 'o', 'g'], ['y', 'y', 'g', 'y', 'y', 'o', 'b', 'r']])
    