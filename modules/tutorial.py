import pyautogui as pag

import modules.utils as utils

def run():
    print('Starting tutorial...')

    print('\tSkipping Ayumu...')

    utils.skipStory()
    
    print('\tSkipping first song tutorial...')

    utils.skipInfoBlock(6)
    utils.skipTutorialSong()
    
    print('\tFinishing first song tutorial...')
    
    for x in range(3):
        pag.click(utils.waitForImage('images/tap-screen-1.png'))

    print('\tGoing to second song tutorial...')

    utils.skipStory()

    print('\tSkipping second song tutorial...')

    utils.skipInfoBlock(7)
    utils.skipTutorialSong()

    print('\tFinishing second song tutorial...')

    for x in range(3):
        pag.click(utils.waitForImage('images/tap-screen-2.png'))

    print('\tSelecting Kotori as partner...')

    pag.click(utils.waitForImage('images/close-large.png', delay=0.5))
    pag.click(utils.waitForImage('images/kotori-char-sel.png'))
    pag.click(utils.waitForImage('images/ok-large.png'))
    utils.waitForImage('images/obtained-sr-school-idol.png')
    pag.click(utils.waitForImage('images/ok-large.png'))

    print('\tSkipping bond tutorial...')

    pag.click(utils.waitForImage('images/next-large.png'))
    pag.click(utils.waitForImage('images/close-large.png'))
    pag.click(utils.waitForImage('images/kotori-bond-tutorial.png'))
    utils.waitForImage('images/cfa-tutorial-1.png')
    pag.click(utils.waitForImage('images/school-idols.png'))
    pag.click(utils.waitForImage('images/practice.png'))

    print('\tStarting practice tutorial...')

    pag.click(utils.waitForImage('images/close-large.png'))
    utils.waitForImage('images/cfa-tutorial-2.png')
    pag.click(utils.waitForImage('images/sr-kotori-tutorial.png'))
    utils.waitForImage('images/cfa-tutorial-3.png')
    pag.click(utils.waitForImage('images/level-up.png'))
    utils.waitForImage('images/cfa-tutorial-4.png')
    pag.click(utils.waitForImage('images/plus.png'))
    utils.waitForImage('images/cfa-tutorial-5.png')
    pag.click(utils.waitForImage('images/level-up-2.png'))
    utils.waitForImage('images/cfa-tutorial-6.png')
    pag.click(utils.waitForImage('images/cancel-2.png'))
    pag.click(utils.waitForImage('images/close-large.png'))

    print('\tIdolizing Kotori...')

    utils.waitForImage('images/cfa-tutorial-7.png')
    pag.click(utils.waitForImage('images/idolize-tutorial.png'))
    pag.click(utils.waitForImage('images/use-items.png'))
    pag.click(utils.waitForImage('images/idolized-kotori.png', delay=1))
    pag.click(utils.waitForImage('images/close-large.png'))
    pag.click(utils.waitForImage('images/cancel.png'))
    pag.click(utils.waitForImage('images/close-large.png'))
    utils.waitForImage('images/cfa-tutorial-8.png')
    pag.click(utils.waitForImage('images/menu.png'))
    utils.waitForImage('images/cfa-tutorial-9.png')
    pag.click(utils.waitForImage('images/school-idols.png'))
    pag.click(utils.waitForImage('images/show-formation-tutorial.png'))
    
    print('\tStarting formation tutorial...')

    utils.skipInfoBlock(2)
    utils.waitForImage('images/cfa-tutorial-10.png')
    pag.click(utils.waitForImage('images/auto-formation.png'))
    utils.waitForImage('images/cfa-tutorial-11.png')
    pag.click(utils.waitForImage('images/recommended-formation.png'))
    pag.click(utils.waitForImage('images/confirm-large.png'))
    utils.waitForImage('images/outfit-no-loading-tutorial.png')
    utils.skipInfoBlock(1)

    print('\tChanging Kotori\'s outfit...')

    utils.waitForImage('images/cfa-tutorial-12.png')
    pag.click(utils.waitForImage('images/change.png'))
    utils.waitForImage('images/cfa-tutorial-13.png')
    pag.click(utils.waitForImage('images/fresh-fruit-parlor.png'))
    utils.waitForImage('images/cfa-tutorial-14.png')
    pag.click(utils.waitForImage('images/ok-large.png'))
    utils.waitForImage('images/cfa-tutorial-15.png')
    pag.click(utils.waitForImage('images/menu.png'))
    pag.click(utils.waitForImage('images/story-tutorial.png'))
    
