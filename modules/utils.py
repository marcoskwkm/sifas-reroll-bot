import pyautogui as pag
import time

def waitForColorAtPosition(colors, positions):
    while True:
        img = pag.screenshot()
        for (pos, color) in zip(positions, colors):
            if img.getpixel(pos) == color:
                return (color, pos)
        time.sleep(0.1)

def waitForImage(path):
    while True:
        pos = pag.locateCenterOnScreen(path, confidence=0.9)
        if pos != None:
            return pos
