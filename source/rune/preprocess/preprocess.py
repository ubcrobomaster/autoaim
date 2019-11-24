import os
from pathlib import Path

from source.common.module import Module


class Preprocess(Module):
    def __init__(self, state=None):
        self.working_dir = Path(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(self.working_dir, state=state)

    def process(self, frame, rune_center):
        frame = frame.copy()
        dims = frame.shape[:2]
        top = round((dims[0] * (1 - self.properties["y_scaling"])) * rune_center[1])
        bottom = dims[0] - top
        left = round((dims[1] * (1 - self.properties["x_scaling"])) * rune_center[0])
        right = dims[1] - left
        crop_img = frame[top:bottom, left:right]
        return crop_img