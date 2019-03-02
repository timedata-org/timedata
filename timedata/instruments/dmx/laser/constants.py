import enum


@enum.unique
class Channels(enum.IntEnum):
    MODE = 0
    PATTERN = 1
    ZOOM = 2
    XROT = 3
    YROT = 4
    ZROT = 5
    HPOS = 6
    VPOS = 7
    COLOR = 8


@enum.unique
class Colors(enum.IntEnum):
    ALL = 0
    RED = 64
    GREEN = 96
    BLUE = 128
    YELLOW = 160
    PINK = 192
    CYAN = 224


@enum.unique
class Patterns(enum.IntEnum):
    CIRCLE = 0
    SPIKE_CIRCLE = 8
    TRIANGLE = 16
    SQUARE = 24
    SPIKE_SQUARE = 32
    SQUARE_IN_SQUARE = 40
    MALTESE_CROSS = 48
    STAR = 56
    ELL = 64
    HOURGLASS = 72
    SPIRAL = 80
    CEES = 88
    LOGARITHMIC = 96
    TWO_QUARTER_CIRCLE = 104
    SPECS = 112
    WAVE = 120
    VEE = 128
    EM = 136
    SAW = 144
    LINE = 152
    THREE_LINES = 160
    JOINED_LINE = 168
    PARALLEL_LINES = 176
    X = 184
    SKEW = 192
    FOUR_LINES = 200
    TWO_SQUARES = 208
    FOUR_SQUARES = 216
    ONE_INTENSE_SQUARE = 224
    DOTTED_LINE = 232
    DOTTED_SEMICIRCLE = 240
    RANDOM_DOTS = 248
