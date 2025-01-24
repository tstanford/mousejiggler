import math
import time 
import usb_hid
import board
from adafruit_hid.mouse import Mouse
from digitalio import DigitalInOut, Direction, Pull

def main():
    button = DigitalInOut(board.GP17)
    button.direction = Direction.INPUT
    button.pull = Pull.UP

    led = DigitalInOut(board.GP16)
    led.direction = Direction.OUTPUT

    state=0
    prev = (0,0)
    
    while True:
        state = handleButton(button, led, state)
        previous_state = state
        if state == 1:
            for zi in range(0,int((math.pi*2)*10)):
                z = float(zi)/10
                x = math.sin(z)
                y = math.cos(z)
                
                deltax = prev[0]-x;
                deltay = prev[1]-y;

                try:
		    move(int(deltax*150), int(deltay*150))
                except:
                    break

                prev = (x,y)
                time.sleep(0.01)
                state = handleButton(button, led, state)

            start = time.time()
            while time.time() - start < 30:
                if state != previous_state:
                    print("stopping")
                    break
                
                state = handleButton(button, led, state)
                time.sleep(0.1)
                print("tick")
        else:
            print("not moving mouse")
            time.sleep(0.1)

def handleButton(button, led, state):
    if button.value == False:
        print("button press")
        state = 1 if state == 0 else 0
        led.value = state
        while(button.value == False):
            time.sleep(0.01)
    led.value = state
    return state

def move(x,y):
    mouse = Mouse(usb_hid.devices)
    mouse.move(x, y, 0)


if __name__ == '__main__':
    main()
