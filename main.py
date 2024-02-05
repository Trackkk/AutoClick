import time
import keyboard
import pyautogui
import win32api
import win32con
from pyautogui import ImageNotFoundException

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not keyboard.is_pressed('q'):
    try:
        # Megkeressuk a kepet a kepernyon
        pic = pyautogui.locateCenterOnScreen("MentesGomb.png")
        if pic is not None:
            x, y = pic
            click(x, y)
            print("Image found and clicked.")
    except ImageNotFoundException:
        print("Image not found on the screen.")
    except KeyboardInterrupt:
        print("Code closed.")
    # Delay hogy ne spameljen
    time.sleep(0.05)
