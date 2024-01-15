#! python3
# 20lookingBusy.py - Nudging mouse cursor every 10 seconds

import pyautogui, time

while True:
    pyautogui.move(1, 0, duration=1)
    time.sleep(10)
    pyautogui.move(-1, 0, duration=1)
    time.sleep(10)

