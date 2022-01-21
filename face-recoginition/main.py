import cv2

from frame_extract import get_contours


def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        _, image = cam.read()

        image = cv2.flip(image, 1)
        _, contours = get_contours(image)

        # cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
        draw_bounding_rect(image, contours)
        cv2.imshow('RubexCubex', image)

        if cv2.waitKey(1) == 27: 
            break
    
    cv2.destroyAllWindows()

def draw_bounding_rect(image, bounding_rects):
    for bounding_rect in bounding_rects:
        (x, y, w, h) = bounding_rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)


def main():
    show_webcam()


if __name__ == '__main__':
    main()
