import pyautogui as pag
import time

import modules.resetSIFID as resetSIFID
import modules.registration as registration

time.sleep(2)
resetSIFID.run()
registration.run()
