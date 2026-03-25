import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.extensions.ble import BLE

keyboard = KMKKeyboard()

ble = BLE()
keyboard.extensions.append(ble)

macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (
    board.D2, board.D3, board.D4,
    board.D5, board.D6, board.D7,
    board.D8, board.D9, board.D10
)

keyboard.row_pins = (board.D1,)
keyboard.diode_orientation = keyboard.DIODE_COL2ROW

led = digitalio.DigitalInOut(board.D11)
led.direction = digitalio.Direction.OUTPUT
led.value = False

open_terminal = KC.MACRO(
    KC.LGUI(KC.SPACE),
    KC.DELAY(200),
    "terminal",
    KC.ENTER
)

open_youtube = KC.MACRO(
    KC.LGUI(KC.SPACE),
    KC.DELAY(200),
    "youtube",
    KC.ENTER
)

open_vscode = KC.MACRO(
    KC.LGUI(KC.SPACE),
    KC.DELAY(200),
    "visual studio code",
    KC.ENTER
)

open_kicad = KC.MACRO(
    KC.LGUI(KC.SPACE),
    KC.DELAY(200),
    "kicad",
    KC.ENTER
)

screenshot = KC.LGUI(KC.LSHIFT(KC.FOUR))
vscode_terminal = KC.LCTL(KC.GRAVE)

keyboard.keymap = [
    [
        KC.VOLD,
        KC.MUTE,
        KC.VOLU,
        open_terminal,
        open_youtube,
        open_vscode,
        screenshot,
        vscode_terminal,
        open_kicad
    ]
]

def before_matrix_scan(keyboard):
    pressed = any([not pin.value for pin in keyboard.matrix.columns])
    led.value = pressed

keyboard.before_matrix_scan = before_matrix_scan

if __name__ == '__main__':
    keyboard.go()