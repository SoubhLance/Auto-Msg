import pyautogui
import time

print("Starting PyAutoGUI automation...")

try:
    time.sleep(5)  # Small delay
    
    for i in range(100):
        message = f"Spamming Ha Ha #{i+1}"
        print(f"Typing: {message}")
        pyautogui.write(message, interval=0.01)
        pyautogui.press("enter")
    
    print("Automation completed successfully!")
    
except Exception as e:
    print(f"Error in automation: {e}")
     


