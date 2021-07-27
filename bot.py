import time
import keyboard
import pyautogui
import win32api
import win32con

# 225, 219, 195

time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def screenshot():
    left = 656
    top = 335
    width = 610
    height = 430

    pic = pyautogui.screenshot(region=(left, top, width, height))

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))
            if b == 195:
                click((x + left), (y + top))
                time.sleep(0.1)
                break


while not keyboard.is_pressed('q'):
    screenshot()
