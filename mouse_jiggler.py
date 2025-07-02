import pyautogui
import time

def keep_mouse_alive(interval_seconds=5):
    print("Mouse jiggler started. Press Ctrl+C to stop.")
    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()
            # Move the mouse slightly and move it back
            pyautogui.moveTo(x + 5, y)
            pyautogui.moveTo(x, y)
            print(f"Mouse moved at {time.strftime('%H:%M:%S')}")
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\nMouse jiggler stopped by user.")

if __name__ == "__main__":
    keep_mouse_alive(5)
