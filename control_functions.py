import os
import time
import random
import importlib

# Check for "device_list.py" and create it if not found
open('device_list.py', 'a').close()
if os.stat('device_list.py').st_size == 0:
    with open('device_list.py', 'a') as file:
        file.write("macs = {\n\t\n}")
from a_device_list import macs

def hexc(dec):
    '''
    take a decimal number and format it to hex without "oX", 
    using uppercase and making sure its 2 digits long.
    '''
    return format(dec, "X").zfill(2)

def send_colour_code(r,g,b,mac):
    checksum = 52^r^g^b #52 is a magic number (0x34)
    checksum = hexc(checksum)
    # print(checksum)
    command = f"gatttool -b {mac} --char-write-req --handle 0x0015 --value 330502{hexc(r)}{hexc(g)}{hexc(b)}00000000000000000000000000{checksum}"
    # print (command)
    os.system(command)

def send_brightness(brightness, mac):
    checksum = hexc(0x33^0x04^brightness)
    command = f"gatttool -b {mac} --char-write-req --handle 0x0015 --value 3304{hexc(brightness)}00000000000000000000000000000000{checksum}"
    os.system(command)


def lightshowone():
    '''flash random colours at full brightness'''
    for _ in range(0,500):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        for mac in macs.values():
            send_colour_code(r,g,b, mac)
            time.sleep(0.05)


if __name__ == "__main__":
    if len(macs.keys()) > 0:
        for x in range(0,255, 5):
            send_brightness(255-x, macs.values[0])
        for x in range(0,255, 5):
            send_brightness(x, macs.values[0])
        lightshowone()