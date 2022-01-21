import re
from email.mime import image

import cv2
import numpy as np
from cv2 import erode


class ContourContainer:

    def __init__(self, contour) -> None:
        self.contour = contour
        self.epsilon=0.01*cv2.arcLength(contour, True)
        self.approx = cv2.approxPolyDP(contour, self.epsilon, closed=True)
        self.bounding_rect = cv2.boundingRect(self.approx)

def get_contours(frame):
    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)[:,:,2]

    blurred = cv2.GaussianBlur(gray_frame, (15, 15), 0)
    canny = cv2.Canny(blurred, 10, 20, 3)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    dilated = cv2.dilate(canny, kernel)

    (contours, _) = cv2.findContours(dilated.copy(), 
                                         cv2.RETR_TREE,
                                         cv2.CHAIN_APPROX_SIMPLE)
    
    contour_containers = [ContourContainer(contour) for contour in contours]
    squerishContours = [contour_container for contour_container in contour_containers if is_square(contour_container)]

    # approx = [contour_container.approx for contour_container in squerishContours]
    approx = [contour_container.approx for contour_container in get_cube_countours(squerishContours)]

    return dilated, approx

def get_cube_countours(squerishContours):
    
    neighbours = {}

    for contour in squerishContours:
        test_bounding_rects = get_neighbour_bounding_rects(contour.bounding_rect)
        neighbours[contour] = []
        for neighbour in squerishContours:
            (x, y, w, h) = neighbour.bounding_rect
            for (neig_x, neig_y) in test_bounding_rects:
                 if (x < neig_x and y < neig_y) and (x + w > neig_x and y + h > neig_y):
                        neighbours[contour].append(neighbour)
    
    for key, value in neighbours.items():
        if len(value) >= 8:
            return value + [key]

    return []

def get_neighbour_bounding_rects(root_bounding_box):
    (x, y, w, h) = root_bounding_box
    center = (x + w/2, y + h/2)
    radius = 1.5

    top_left = (center[0] - w * radius, center[1] - h * radius)
    top_mid = (center[0], center[1] - h * radius)
    top_right = (center[0] + w * radius, center[1] - h * radius)
    
    mid_left = (center[0] - w * radius, center[1])
    mid_right = (center[0] + w * radius, center[1])

    bot_left = (center[0] - w * radius, center[1] + h * radius)
    bot_mid = (center[0], center[1] + h * radius)
    bot_right = (center[0] + w * radius, center[1] + h * radius)

    return [top_left, top_mid, top_right, top_left, mid_left, mid_right, bot_left, bot_mid, bot_right]

def is_square(contour_container):
    return len(contour_container.approx) > 4 and isSquerish(contour_container)

def isSquerish(contour_container):
    area = cv2.contourArea(contour_container.contour)
    (x, y, w, h) = contour_container.bounding_rect

    # Find aspect ratio of boundary rectangle around the countours.
    ratio = w / float(h)

    # Check if contour is close to a square.
    if ratio >= 0.8 and ratio <= 1.2 and w >= 30 and w <= 60 and area / (w * h) > 0.4:
        return True
    
    return False

def sort_corners(corners):

    return []
