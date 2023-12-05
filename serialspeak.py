#!/usr/bin/env python3

import serial
import espeak
import sys


def listen(serdev):
    ser = serial.Serial(serdev, 1200)
    espeak.init()
    speaker = espeak.Espeak()
    speaker.voice["language"] = "it"

    terminators = [0x0D, 0x0A]
    while True:
        line = bytearray()
        while True:
            ch = ser.read(1)
            if ch[0] in terminators:
                break
            else:
                line += ch
        if len(line) > 0:
            line = line.decode().strip()
            print(f"got [{line}]")
            speaker.say(line)


if __name__ == "__main__":
    listen(sys.argv[1])
