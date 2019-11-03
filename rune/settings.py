# square frame with side length FRAME_DIM
FRAME_DIM = 300
WHEEL_RAD = round(0.4 * FRAME_DIM)
TARGET_RAD = round(0.87 * WHEEL_RAD)
MASK_RAD = round(0.6 * WHEEL_RAD)
MASK_DIM = round(0.1 * WHEEL_RAD)
FRAME_CNTR = (round(FRAME_DIM/2), round(FRAME_DIM/2))

R_DIM = round(0.034 * FRAME_DIM)
CNTR_DIM = round(2.5 * R_DIM)
WHEEL_R_INC = round(0.2 * R_DIM)
CNTR_OFFSET = (round(-0.2 * R_DIM), round(0.45 * R_DIM))

WHEEL_RECNTR_FREQ = 18
WHEEL_ROTDIR_CNT = 3

# colors in BGR space
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)


ANGLE_INC = 2  # choose a divisor of 72 (1, 2, 3, 4, 6, ...)
ANGLE_MAX = 360
CNT_PANELS = 5
ANGLE_SEP = round(ANGLE_MAX / CNT_PANELS)
ANGLE_ESTIMATE_DIST = 5
ANGLE_NBHD = ANGLE_SEP - ANGLE_ESTIMATE_DIST
DEG_TO_RAD = 3.1415 / 180
ANGLE_VALS = range(0, ANGLE_MAX, ANGLE_INC)

INC_ANGLE_MAX = round(ANGLE_MAX / ANGLE_INC)
INC_ANGLE_SEP = round(ANGLE_SEP / ANGLE_INC)
INC_ANGLE_NBHD = round(ANGLE_NBHD / ANGLE_INC)

LUM_MAX = 255
LUM_THRESH_BW = round(0.85 * LUM_MAX)
LUM_THRESH_LOW = round(0.3 * LUM_MAX)
LUM_THRESH_HIGH = round(0.6 * LUM_MAX)

ANGULAR_SPEED = 60  # degrees per second

STATE_ACTIVE = '1'
STATE_ACTIVATING = 'A'
STATE_INACTIVE = '-'
