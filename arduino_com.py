# This file handels with the serial communication between the Arduino nano and the raspberry Pi
import serial
import time
msgs = [b"0\n", b"1\n", b"2\n", b"3\n", b"4\n", b"5\n", b"6\n", b"7\n"]

if __name__ =='__main__':
    ser=seiral.Serial('/dev/ttyACM0',9600,timeout=1)
    ser.flush()
    while True:
        for m in msgs:
            ser.write(m)
            line=ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1);