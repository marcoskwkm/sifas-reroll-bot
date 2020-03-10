import pyautogui as pag

import modules.utils as utils

def skipOpeningCutscene():
    print('\tSkipping opening cutscene...')

    pag.click(utils.waitForImage('images/opening-animation.png'))
    pag.click(utils.waitForImage('images/ok.png'))

def startDownload():
    print('\tStarting download...')

    pag.click(pag.locateCenterOnScreen('images/start.png', confidence=0.9))

    # TODO: Treat case when download continues after skipping opening cutscene.

def run():
    print('Registration...')

    print('\tReopening SIFAS...')

    pag.click(utils.waitForImage('images/sifas.png'))

    pag.click(utils.waitForImage('images/parental-consent.png'))
    pag.click(utils.waitForImage('images/klab-games.png'))
    pag.click(utils.waitForImage('images/sunrise.png'))
    pag.click(utils.waitForImage('images/bushiroad.png'))
    pag.click(utils.waitForImage('images/9th-anniversary.png'))
    pag.click(utils.waitForImage('images/title.png'))

    print('\tAgreeing to terms...')

    pag.click(utils.waitForImage('images/agree.png'))

    print('\tChecking for downloads...')

    while True:
        if pag.locateOnScreen('images/start.png', confidence=0.9) != None:
            startDownload()
            break
        if pag.locateOnScreen('images/opening-animation.png', confidence=0.9) != None:
            break

    skipOpeningCutscene()

    print('\tRegistering player...')

    pag.click(utils.waitForImage('images/tap-to-input.png'))
    okPos = utils.waitForImage('images/input-ok.png')
    pag.typewrite('f')
    pag.click(okPos)
    pag.click(utils.waitForImage('images/next-large.png'))

    pag.click(utils.waitForImage('images/tap-to-input.png'))
    okPos = utils.waitForImage('images/input-ok.png')
    pag.typewrite('f')
    pag.click(okPos)
    pag.click(utils.waitForImage('images/next.png'))

    pag.click(utils.waitForImage('images/ok.png'))

    pag.click(utils.waitForImage('images/confirm.png'))

    pag.click(utils.waitForImage('images/yes-large.png'))
    
    
