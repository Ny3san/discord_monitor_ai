import pyautogui, os
def capture_screen(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pyautogui.screenshot().save(path)
