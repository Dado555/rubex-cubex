from collections import Counter

import cv2

from color_detection import ColorDetector
from frame_extract import get_contours


class RubexCubex:

    def __init__(self):
        self.faces = {}
        self.preview_state = {}
        self.face_states = {}
    
    def export_faces(self):
        return ""

    def add_face(self):
        print(self.preview_state)
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
        print(self.faces)
    
def show_webcam():
    cube = RubexCubex()
    color_detector = ColorDetector()
    in_calibration_mode = False
    calibration_colors = {}
    colors = ['green', 'red', 'blue', 'orange', 'white', 'yellow']
    calibration_counter = 0
    
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

        if in_calibration_mode and contours:
            
            # add color
            if cv2.waitKey(1) == ord('a'):
                color_in_area = color_detector.get_dominant_color(image, contours[4])
                calibration_colors[colors[calibration_counter]] = color_in_area
                print("entered " + colors[calibration_counter])
                calibration_counter += 1

            if calibration_counter == len(colors):
                in_calibration_mode = False
                color_detector.set_colors(calibration_colors)
                print("done calibrating...")
                print(calibration_colors)
            else:
                contours = [contours[4]]
        else:
            new_state = color_detector.estimate_colors(image, contours)
            if new_state != {}:
                cube.update_preview_state(new_state)

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

def main():
    show_webcam()


if __name__ == '__main__':
    main()
