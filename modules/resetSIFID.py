import pyautogui as pag
import time

import modules.positions as positions
import modules.utils as utils

CLOSE_BUTTON_XY = (1307, 821)
CLOSE_BUTTON_RGB = (100, 100, 100)
FILE_MANAGER_XY = [(956, 395), (942, 819), (961, 213)]
FILE_MANAGER_RGB = [(28, 127, 214), (30, 135, 227), (25, 113, 190)]
TEXT_XY = (316, 715)
SELECT_ALL_XY = (1350, 123)
SELECT_ALL_RGB = (242, 242, 242)
SAVE_BUTTON_XY = (1601, 127)
HOME_BUTTON_XY = (1898, 991)

def run():
    print('Resetting SIFID...')

    print('\tClosing SIFAS...')

    pag.click(*positions.TASKS_BUTTON_XY)
    utils.waitForColorAtPosition([CLOSE_BUTTON_RGB], [CLOSE_BUTTON_XY])
    pag.click(CLOSE_BUTTON_XY)

    print('\tOpening File Manager...')

    _, fmPos = utils.waitForColorAtPosition(FILE_MANAGER_RGB, FILE_MANAGER_XY)
    pag.click(fmPos)

    print('\tErasing playerprefs.xml...')

    time.sleep(2)

    pag.mouseDown(TEXT_XY)
    utils.waitForColorAtPosition([SELECT_ALL_RGB], [SELECT_ALL_XY])
    pag.mouseUp()
    pag.click(SELECT_ALL_XY)
    pag.typewrite(['backspace'])

    print('\tWriting playerprefs.xml...')

    with open('playerprefs.xml', 'r') as playerPrefsFile:
        for line in playerPrefsFile.readlines():
            pag.typewrite(line.rstrip())
            time.sleep(len(line.rstrip()) * 0.01)
            pag.typewrite('\n')

    print('\tSaving playerprefs.xml...')

    pag.click(SAVE_BUTTON_XY)

    print('\tGoing to home screen...')

    pag.click(positions.HOME_BUTTON_XY)
