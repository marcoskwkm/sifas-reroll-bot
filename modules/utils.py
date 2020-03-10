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

def waitForImage(path, delay=0, timeout=0):
    startTime = time.perf_counter()
    while True:
        pos = pag.locateCenterOnScreen(path, confidence=0.9)
        if pos != None:
            time.sleep(delay)
            return pos
        if timeout > 0 and time.perf_counter() - startTime > timeout:
            raise TimeoutError('Could not find image %s' % path)

def skipStory():
    pag.click(waitForImage('images/open-story-menu.png'))
    pag.click(waitForImage('images/menu-skip.png'))
    pag.click(waitForImage('images/ok.png'))

def skipTutorialSong():
    pag.click(waitForImage('images/song-pause.png'))
    pag.click(waitForImage('images/ok.png'))

def skipInfoBlock(n):
    for x in range(n - 1):
        pag.click(waitForImage('images/next-large.png'))
    pag.click(waitForImage('images/close-large.png'))
