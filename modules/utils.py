import pyautogui as pag
import time

class TimeoutError(Exception):
    pass

def waitForColorAtPosition(colors, positions):
    while True:
        img = pag.screenshot()
        for (pos, color) in zip(positions, colors):
            if img.getpixel(pos) == color:
                return (color, pos)
        time.sleep(0.1)

def waitForImage(path, timeout=0):
    startTime = time.perf_counter()
    while True:
        pos = pag.locateCenterOnScreen(path, confidence=0.9)
        if pos != None:
            return pos
        if timeout > 0 and time.perf_counter() - startTime > timeout:
            raise TimeoutError('Could not find image %s' % path)
