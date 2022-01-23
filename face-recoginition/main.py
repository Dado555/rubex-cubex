import cv2

from color_detection import ColorDetector
from frame_extract import get_contours


def show_webcam():

    color_detector = ColorDetector()
    preview_state = {}
    in_calibration_mode = False
    calibration_colors = {}
    colors = ['green', 'blue', 'red', 'yellow', 'orange', 'white']
    calibration_counter = 0
    
    cam = cv2.VideoCapture(0)
    while True:
        _, image = cam.read()

        image = cv2.flip(image, 1)
        _, contours = get_contours(image)

        if cv2.waitKey(1) == ord('c'): 
            in_calibration_mode = not in_calibration_mode

        if cv2.waitKey(1) == 27: 
            break

        if in_calibration_mode and contours:
            
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
            if new_state != preview_state:
                preview_state = new_state
                print(preview_state)

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
