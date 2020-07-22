# simulate mouse usage
from pynput.mouse import Button, Controller
import sys
import time

def run():
    if len(sys.argv) != 2:
        print("Args != 2")
        sys.exit()

    mouse = Controller()

    # hit shot with mouse positions
    hit_shot(mouse)

def hit_shot(mouse):
    mouse.position = (975, 500)
    mouse.click(Button.left)
    mouse.press(Button.left)
    time.sleep(0.25)
    mouse.move(0, -425)
    time.sleep(0.25)
    mouse.release(Button.left)
    time.sleep(2.25)
    mouse.click(Button.left, 2)



run()
    