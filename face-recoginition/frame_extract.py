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
    hsv_value = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)[:,:,2]
    blurred = cv2.GaussianBlur(hsv_value, (15, 15), 0)
    canny = cv2.Canny(blurred, 10, 20, 3)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    dilated = cv2.dilate(canny, kernel)

    (contours, hierarchy) = cv2.findContours(dilated.copy(), 
                                         cv2.RETR_TREE,
                                         cv2.CHAIN_APPROX_SIMPLE)
    
    hasChild = hierarchy[0, :, 2]
    nonParentContourIndexes = (hasChild == -1).nonzero()[0]
    contours = [contours[i] for i in nonParentContourIndexes]
    
    contour_containers = [ContourContainer(contour) for contour in contours]
    squerishContours = [contour_container for contour_container in contour_containers if is_square(contour_container)]

    # approx = [contour_container.approx for contour_container in squerishContours]
    bounding_rects = [contour_container.bounding_rect for contour_container in get_cube_countours(squerishContours)]

    y_sorted = sorted(bounding_rects, key=lambda item: item[1])

    top_row = sorted(y_sorted[0:3], key=lambda item: item[0])
    middle_row = sorted(y_sorted[3:6], key=lambda item: item[0])
    bottom_row = sorted(y_sorted[6:9], key=lambda item: item[0])

    sorted_bounding_rects = top_row + middle_row + bottom_row

    return dilated, sorted_bounding_rects

def get_cube_countours(squerishContours):
    
    neighbours = {}

    for contour in squerishContours:
        test_bounding_rects = get_neighbour_bounding_rects(contour.bounding_rect)
        neighbours[contour] = []
        for neighbour in squerishContours:
            if neighbour == contour:
                continue
            (x, y, w, h) = neighbour.bounding_rect
            for (neig_x, neig_y) in test_bounding_rects:
                 if (x < neig_x and y < neig_y) and (x + w > neig_x and y + h > neig_y):
                        if neighbour not in neighbours[contour]: 
                            neighbours[contour].append(neighbour)
    
    for key, value in neighbours.items():
        if len(value) == 8:
            return value + [key]

    return []

def get_neighbour_bounding_rects(root_bounding_box):
    (x, y, w, h) = root_bounding_box
    center = (x + w/2, y + h/2)
    radius = 1.3

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
    return len(contour_container.approx) >= 4 and isSquerish(contour_container)

def isSquerish(contour_container):
    area = cv2.contourArea(contour_container.contour)
    (x, y, w, h) = contour_container.bounding_rect

    # Find aspect ratio of boundary rectangle around the countours.
    ratio = w / float(h)

    # Check if contour is close to a square.
    if ratio >= 0.8 and ratio <= 1.2 and w >= 30 and w <= 60 and area / (w * h) > 0.4:
        return True
    
    return False
