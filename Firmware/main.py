import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()
m = Macros()
keyboard.modules.append(m)

rgb = RGB(
    pixel_pin=board.GP6,
    num_pixels=2,
    hue_default=180,
    sat_default=100,
    val_default=60
)
keyboard.modules.append(rgb)

PINS = [
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP29,
    board.GP7,
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3
]

keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

T1 = KC.LCTRL(KC.LALT(KC.T))
YT = KC.LCTRL(KC.LALT(KC.Y))
VS = KC.LCTRL(KC.LALT(KC.V))
KI = KC.LCTRL(KC.LALT(KC.K))

keyboard.keymap = [
    [
        KC.VOLD,
        KC.MUTE,
        KC.VOLU,
        T1,
        YT,
        VS,
        KC.PSCR,
        KC.LCTRL(KC.GRV),
        KI
    ]
]

if __name__ == '__main__':
    keyboard.go()
