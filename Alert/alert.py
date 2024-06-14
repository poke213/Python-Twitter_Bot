import ctypes
import time

def popup(title, text):
    ctypes.windll.user32.MessageBoxW(0, text, title, 1)

while True:
    popup("Alert", "Walk break")
    time.sleep(1800)  # Sleep for 30 minutes