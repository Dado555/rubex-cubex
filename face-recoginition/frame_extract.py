import re
from email.mime import image

import cv2
import numpy as np


class ContourContainer:

    def __init__(self, contour) -> None:
        self.contour = contour
        self.epsilon=0.01*cv2.arcLength(contour, True)
        self.approx = cv2.approxPolyDP(contour, self.epsilon, closed=True)

def get_contours(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_frame, (3, 3), 0)
    canny = cv2.Canny(blurred, 15, 30, 3)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilated = cv2.dilate(canny, kernel, iterations=2)

    (contours, _) = cv2.findContours(dilated.copy(), 
                                         cv2.RETR_TREE,
                                         cv2.CHAIN_APPROX_SIMPLE)
    
    contour_containers = [ContourContainer(contour) for contour in contours]
    approx = [contour_container.approx for contour_container in contour_containers if is_square(contour_container)]

    return approx

def is_square(contour_container):
    return len(contour_container.approx) > 4 and isSquerish(contour_container)

def isSquerish(contour_container):
    area = cv2.contourArea(contour_container.contour)
    (x, y, w, h) = cv2.boundingRect(contour_container.approx)

    # Find aspect ratio of boundary rectangle around the countours.
    ratio = w / float(h)

    # Check if contour is close to a square.
    if ratio >= 0.8 and ratio <= 1.2 and w >= 30 and w <= 60 and area / (w * h) > 0.4:
        return True
    
    return False

def sort_corners(corners):

    return []
