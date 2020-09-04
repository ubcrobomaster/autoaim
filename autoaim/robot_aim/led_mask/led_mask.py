from assets.module import Module
from pathlib import Path
import os
import cv2
import numpy as np


class LedMask(Module):
    def __init__(self, parent, **config):
        self.wd = Path(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(self.wd, parent, config)
        frame_height = parent.robot_crop.config['dims'][1]
        self.config['dilate'] = round(self.config['dilate_rel'] * frame_height)
        self.config['morph'] = [round(val * frame_height) for val in self.config['morph_rel']]

    def process(self, roi):
        """
        :return: B&W led mask of ROI. Value of each pixel is 0 or 255.
        """
        mask = cv2.inRange(roi, tuple(self.config['range'][0]), tuple(self.config['range'][1]))
        mask = cv2.dilate(mask, np.ones((self.config['dilate'], self.config['dilate'])))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, tuple(self.config['morph']))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        return mask