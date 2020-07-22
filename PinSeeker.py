# simulate mouse usage
from pynput.mouse import Button, Controller
import sys
import time

def run():
    if len(sys.argv) != 3:
        print("Args != 3")
        sys.exit()

    mouse = Controller()

    # hit shot with mouse positions
    if sys.argv[1] == "driver":
        hit_driver(mouse)
    elif sys.argv[1] == "iron":
        hit_iron(mouse)
    

def hit_driver(mouse):
    mouse.position = (975, 500) 
    time.sleep(0.25)

    if sys.argv[2] == "100":
        mouse.click(Button.left)
        time.sleep(1)
        mouse.press(Button.left)
        time.sleep(0.25)
        mouse.move(0, -425)
        time.sleep(0.25)
        mouse.release(Button.left)
        time.sleep(2.18)
        mouse.click(Button.left, 2)
    elif sys.argv[2] == "95":
        mouse.click(Button.left)
        time.sleep(1)
        mouse.press(Button.left)
        time.sleep(0.25)
        mouse.move(0, -381)
        #time.sleep(0.25)
        #mouse.release(Button.left)
        #time.sleep(2.18)
        #mouse.click(Button.left, 2)
    elif sys.argv[2] == "90":
        mouse.click(Button.left)
        time.sleep(1)
        mouse.press(Button.left)
        time.sleep(0.25)
        mouse.move(0, -363)
        #time.sleep(0.25)
        #mouse.release(Button.left)
        #time.sleep(2.18)
        #mouse.click(Button.left, 2)
    elif sys.argv[2] == "85":
        mouse.click(Button.left)
        time.sleep(1)
        mouse.press(Button.left)
        time.sleep(0.25)
        mouse.move(0, -345)
        #time.sleep(0.25)
        #mouse.release(Button.left)
        #time.sleep(2.18)
        #mouse.click(Button.left, 2)
    elif sys.argv[2] == "80":
        mouse.click(Button.left)
        time.sleep(1)
        mouse.press(Button.left)
        time.sleep(0.25)
        mouse.move(0, -327)
        #time.sleep(0.25)
        #mouse.release(Button.left)
        #time.sleep(2.18)
        #mouse.click(Button.left, 2)
    

def hit_iron(mouse):
    mouse.position = (975, 500)
    mouse.click(Button.left)
    time.sleep(1)
    mouse.press(Button.left)
    time.sleep(0.25)
    mouse.move(0, -425)
    time.sleep(0.25)
    mouse.release(Button.left)
    time.sleep(1.98)
    mouse.click(Button.left, 2)

run()
    