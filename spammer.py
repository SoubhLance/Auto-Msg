import pyautogui
import time

time.sleep(5)  # Time to focus on chat

for i in range(100):
    pyautogui.write(f"Spam #{i+1}", interval=0.01)
    pyautogui.press("enter")