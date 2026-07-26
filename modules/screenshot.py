#IMPORTING PYAUTOGUI
import pyautogui

import os

#IMPORTING DATE AND TIME TAAKI SCREENSHOT KE NAAM KE AAGE DATE ND TIME AA JAYE TAAKI OVERWRITE NA HO SCREENSHOT
from datetime import datetime




#MISSION 22
#FUCNTION CREATE KAR RHE HAI SCREENSHOT NIKALNE KE LIYE THROUGH JARVIS
def take_screenshot():

    folder = "Screenshots"

    if not os.path.exists(folder):
        os.makedirs(folder)

        

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"Screenshot_{current_time}.png"

    image = pyautogui.screenshot()

    image.save(filename)

    return filename