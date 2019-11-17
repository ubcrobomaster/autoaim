from pathlib import Path
from .module import Module

import imutils
import cv2
import os


def find_contours(thresh):
    """
    gets areas of color from image

    :param thresh: a binary image
    :return: an array of openCV contours
    """
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    return cnts


def get_shape(c):
    """
    finds shape of a contour

    :param c: an openCV contour
    :return: a string of the name of the shape
    """
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)

    if len(approx) == 1:
        shape = "line"

    if len(approx) == 3:
        shape = "triangle"

    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        shape = "square" if 0.95 <= ar <= 1.05 else "rectangle"

    elif len(approx) == 5:
        shape = "pentagon"

    else:
        shape = "circle"

    return shape


def find_quad_centers(contours):
    """
    finds centers of contours that have 4 sides

    :param contours: a list of openCV contours
    :return: a list of coordinates in the form [x,y]
    """
    quads = []

    for c in contours:
        M = cv2.moments(c)
        if M["m00"] == 0.0:
            cX = int(M["m10"] / 0.00001)
            cY = int(M["m01"] / 0.00001)
        else:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

        shape = get_shape(c)

        if shape == "rectangle" or shape == "pentagon":
            c = c.astype("float")
            c = c.astype("int")
            coord = [cX, cY]
            quads.append(coord)

    return quads


def reformat_cv_rectangle(rect):
    """
    converts from an openCV rectangle to a dict style rectangle

    :param rect: an openCV rectangle
    :return: a dictionary rectangle
    """
    rect_dict = {"width": rect[1][0], "height": rect[1][1],
                 "x_center": rect[0][0], "y_center": rect[0][1],
                 "angle": rect[2]}

    return rect_dict


def find_rectangles(filtered):
    """
    finds rectangles around leds

    :param filtered: a binary image of suspected leds
    :return: a list of rectangles in the format ((centerX,centerY),(width,height),(rotation))
    """
    # puts rectangles on blobs
    contours, hierarchy = cv2.findContours(filtered, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rectangles = []
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        if max(rect[1]) > round(filtered.shape[0] / 35) and max(rect[1]) > 2 * min(rect[1]):
            if rect[1][0] > rect[1][1] and rect[2] > -45:
                rect = ((rect[0][0], rect[0][1]), (rect[1][1], rect[1][0]), rect[2] - 90)
            rectangles.append(rect)
    return rectangles


class ShapeFinder(Module):
    def __init__(self):
        self.working_dir = Path(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(self.working_dir)

    def process(self, mask):
        rectangles = find_rectangles(mask)

        leds = []
        for r in rectangles:
            reformat = reformat_cv_rectangle(r)
            leds.append(reformat)
        return leds
