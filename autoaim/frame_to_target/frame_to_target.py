import frame_to_target_config as CONFIG
from frame_to_roi.frame_to_roi import frame_to_roi
from roi_to_mask.roi_to_mask import roi_to_mask
from mask_to_target.mask_to_target import mask_to_target
import cv2


def frame_to_target(frame, debug=CONFIG.DEFAULT_DEBUG):
    debug_frame = frame.copy() if debug else None
    roi = frame_to_roi(frame, debug_frame=debug_frame)
    mask = roi_to_mask(roi, debug_frame=debug_frame)
    target = mask_to_target(mask, debug_frame=debug_frame)

    if debug:
        cv2.imshow(CONFIG.WIN_TITLE, debug_frame)
        cv2.waitKey(CONFIG.FRAME_DELAY)
    return target