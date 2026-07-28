
#MISSION 8: IN THIS WE WILL CALL FUNCTION FROM THIS FILE ie APPS.PY
#WE WILL CALL SYSTEM APPS WITH THIS 

import os


#mission 30: local folder command through open ho rhe basic and imp folders
APP_PATHS = {
    "notepad": "notepad",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

    "calculator": "calc",
    "paint": "mspaint",
    "cmd": "cmd",
    "explorer": "explorer",

    "desktop": os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop"),
    "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "documents": os.path.join(os.path.expanduser("~"), "OneDrive", "Documents"),
    "pictures": os.path.join(os.path.expanduser("~"), "OneDrive", "Pictures"),
    "videos": os.path.join(os.path.expanduser("~"), "OneDrive", "Videos"),
    "music": os.path.join(os.path.expanduser("~"), "OneDrive", "Music"),
}

def open_app(app_name):

    path = APP_PATHS.get(app_name)

    if path:
        print(f"Opening {app_name.title()}, Sir...")

        os.startfile(path)
        return True

    return False

#temporary function



def open_notepad():
    print("Opening Application, Sir..")
    os.system("notepad")

def open_chrome():
    print("Opening Application, Sir..")
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")