import serial, serial.tools.list_ports
import time
from pykeyboard import PyKeyboard
from playsound import playsound

SENSITIVITY = 0.973
BAUDRATE = 115200

print("Connecting...")

ports = serial.tools.list_ports.comports()
if len(ports) == 0:
    print("[ERROR] No devices found, quitting...")
    quit()
elif len(ports) > 1:
    print("[ERROR] There are multiple devices connected, please disconnect except one and try again...")
    quit()

ser = serial.Serial(ports[0].device, BAUDRATE)
print("Connected!")
print("Getting info...")

keyboard = PyKeyboard()
prevLL = 0
while True:
    try:
        incoming = ser.readline().strip()
        lightL = eval(incoming)
        print(lightL)
        if lightL < (1 - SENSITIVITY) * 255 and prevLL > (1 - SENSITIVITY) * 255:
            keyboard.tap_key(keyboard.right_key)
        prevLL = lightL
    except SyntaxError:
        pass
    except KeyboardInterrupt:
        break
