import math
from time import sleep
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

prev = (0,0)

while True:
    for zi in range(0,int((math.pi*2)*10)):
        z = float(zi)/10
        x = math.sin(z)
        y = math.cos(z)
        
        deltax = prev[0]-x;
        deltay = prev[1]-y;

        mouse.move(int(deltax*150), int(deltay*50), 0)

        prev = (x,y)
        sleep(0.01)
    sleep(30)
