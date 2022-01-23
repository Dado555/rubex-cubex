import math
from turtle import distance

import cv2
import numpy as np


def bgr2lab(input_color):
    return xyz2lab(bgr2xyz(input_color))

def bgr2xyz(input_color):
    adjustedBgrValues = np.asarray(input_color)/255

    for index, color in enumerate(adjustedBgrValues):
        if color > 0.04045:
            adjustedBgrValues[index] = ((color + 0.055)/1.055) ** 2.4
        else:
            adjustedBgrValues[index] = color/12.92
        adjustedBgrValues[index] *= 100
    
    [blue, red, green] = adjustedBgrValues
    x = red * 0.4124 + green * 0.3576 + blue * 0.1805
    y = red * 0.2126 + green * 0.7152 + blue * 0.0722
    z = red * 0.0193 + green * 0.1192 + blue * 0.9505
    return [x, y, z]

def xyz2lab(xyz):
    # Observer 2*, Illuminat D65, Daylight
    ref_x = 95.047
    ref_y = 100.000
    ref_z = 108.833

    xyz[0] /= ref_x
    xyz[1] /= ref_y
    xyz[2] /= ref_z

    for index, color in enumerate(xyz):
        if color > 0.008856:
            xyz[index] = color ** (1/3)
        else:
            xyz[index] = 7.787 * color + 16/116
    
    l = (116 * xyz[1]) - 16
    a = 500 * (xyz[0] - xyz[1])
    b = 200 * (xyz[1] - xyz[2])
    return (l, a, b)

# Copyright to https://github.com/lovro-i/CIEDE2000.
def ciede2000(Lab_1, Lab_2):
    C_25_7 = 6103515625 # 25**7

    L1, a1, b1 = Lab_1[0], Lab_1[1], Lab_1[2]
    L2, a2, b2 = Lab_2[0], Lab_2[1], Lab_2[2]
    C1 = math.sqrt(a1**2 + b1**2)
    C2 = math.sqrt(a2**2 + b2**2)
    C_ave = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(C_ave**7 / (C_ave**7 + C_25_7)))

    L1_, L2_ = L1, L2
    a1_, a2_ = (1 + G) * a1, (1 + G) * a2
    b1_, b2_ = b1, b2

    C1_ = math.sqrt(a1_**2 + b1_**2)
    C2_ = math.sqrt(a2_**2 + b2_**2)

    if b1_ == 0 and a1_ == 0: h1_ = 0
    elif a1_ >= 0: h1_ = math.atan2(b1_, a1_)
    else: h1_ = math.atan2(b1_, a1_) + 2 * math.pi

    if b2_ == 0 and a2_ == 0: h2_ = 0
    elif a2_ >= 0: h2_ = math.atan2(b2_, a2_)
    else: h2_ = math.atan2(b2_, a2_) + 2 * math.pi

    dL_ = L2_ - L1_
    dC_ = C2_ - C1_
    dh_ = h2_ - h1_
    if C1_ * C2_ == 0: dh_ = 0
    elif dh_ > math.pi: dh_ -= 2 * math.pi
    elif dh_ < -math.pi: dh_ += 2 * math.pi
    dH_ = 2 * math.sqrt(C1_ * C2_) * math.sin(dh_ / 2)

    L_ave = (L1_ + L2_) / 2
    C_ave = (C1_ + C2_) / 2

    _dh = abs(h1_ - h2_)
    _sh = h1_ + h2_
    C1C2 = C1_ * C2_

    if _dh <= math.pi and C1C2 != 0: h_ave = (h1_ + h2_) / 2
    elif _dh  > math.pi and _sh < 2 * math.pi and C1C2 != 0: h_ave = (h1_ + h2_) / 2 + math.pi
    elif _dh  > math.pi and _sh >= 2 * math.pi and C1C2 != 0: h_ave = (h1_ + h2_) / 2 - math.pi
    else: h_ave = h1_ + h2_

    T = 1 - 0.17 * math.cos(h_ave - math.pi / 6) + 0.24 * math.cos(2 * h_ave) + 0.32 * math.cos(3 * h_ave + math.pi / 30) - 0.2 * math.cos(4 * h_ave - 63 * math.pi / 180)

    h_ave_deg = h_ave * 180 / math.pi
    if h_ave_deg < 0: h_ave_deg += 360
    elif h_ave_deg > 360: h_ave_deg -= 360
    dTheta = 30 * math.exp(-(((h_ave_deg - 275) / 25)**2))

    R_C = 2 * math.sqrt(C_ave**7 / (C_ave**7 + C_25_7))
    S_C = 1 + 0.045 * C_ave
    S_H = 1 + 0.015 * C_ave * T

    Lm50s = (L_ave - 50)**2
    S_L = 1 + 0.015 * Lm50s / math.sqrt(20 + Lm50s)
    R_T = -math.sin(dTheta * math.pi / 90) * R_C

    k_L, k_C, k_H = 1, 1, 1

    f_L = dL_ / k_L / S_L
    f_C = dC_ / k_C / S_C
    f_H = dH_ / k_H / S_H

    dE_00 = math.sqrt(f_L**2 + f_C**2 + f_H**2 + R_T * f_C * f_H)
    return dE_00

colors = {
    'blue': (255, 0, 0),
    'green': (0, 255, 0),
    'red': (0, 0, 255),
    'yellow': (255, 255, 0),
    'orange': (0, 165, 255),
    'white': (255, 255, 255),
}

def get_dominant_color(image, bounding_rect):
    (x, y, w, h) = bounding_rect
    area = image[x:x+w, y:y+h, :]

    area.mean(axis=0).mean(axis=0)
    flat = np.float32(area.reshape(-1, 3))
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    num_of_colors = 1
    _, labels, palette = cv2.kmeans(flat, num_of_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    _, counts = np.unique(labels, return_counts=True)
    dominant = palette[np.argmax(counts)]

    return tuple(dominant)
    

def get_closest_color(input_color):
    distances = []
    for color, value in colors.items():
        distances.append([color, ciede2000(bgr2lab(value), bgr2lab(input_color))])
    closest_color = min(distances, key=lambda distance: distance[1])
    return closest_color


def estimate_colors(image, contours, preview_state):
    for index, contour in enumerate(contours):
        dominant_color = get_dominant_color(image, contour)
        preview_state[index] = get_closest_color(dominant_color)
