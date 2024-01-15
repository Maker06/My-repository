#! python3
# 20readATextField.py - Copying the text from the Notepad to the clipboard

import pyautogui, pyperclip, time

txt = pyautogui.getWindowsWithTitle('Блокнот')[0]

txt.activate()

pyautogui.click(txt.left + 150, txt.top + 150)
#time.sleep(5)

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
text = pyperclip.paste()
print(text)