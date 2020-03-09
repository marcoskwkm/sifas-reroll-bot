import pyautogui as pag

import modules.utils as utils

def run():
    print('Registration...')

    print('\tReopening SIFAS...')

    sifasPos = utils.waitForImage('images/sifas.png')
    pag.click(sifasPos)
