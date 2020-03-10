import pyautogui as pag
import time

import modules.resetSIFID as resetSIFID
import modules.registration as registration
import modules.tutorial as tutorial

time.sleep(2)
resetSIFID.run()
registration.run()
tutorial.run()
