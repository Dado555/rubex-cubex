import cv2

from frame_extract import get_contours


def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        _, image = cam.read()

        image = cv2.flip(image, 1)
        contours = get_contours(image)

        cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
        cv2.imshow('RubexCubex', image)

        if cv2.waitKey(1) == 27: 
            break
    
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()
