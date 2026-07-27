
#THIS IS THE HEART OF JARVIS (main.py )


#Now we will use Git to save the project or making checkpoint to load the file if any error or bug occur in jarvis
#GIT WORKFLOW

#          Working Directory
#        (Tu yaha coding karta hai)
#                  │
#               git add .
#                  │
#                  ▼
#           Staging Area
#         (Git ko bolta hai:
#       "Ye changes save karna.")
#                  │
#         git commit -m "..."
#                  │
#                  ▼
#            Repository
#      (Permanent Snapshot 📸)

#MAIN COMMANDS FOR GITHUB
#git status
#next step

#git add.
#next step

#git commit -m "ADDED ANYTHING"
#next step

#git push





#IMPORTING ALL THE COMMANDS
from modules.command_handlers.commands import execute_command


#MISSION 16: IMPORTING FUNCTION FOR COMMAND
from modules.listening import takeCommand

#Say Function
from modules.speech import say
say("Hello Harshal")




#MISSION 1: JARVIS STARTING
#MISSION 6: TO PUT THIS TWO LINE IN FUNCTION
#actually this was my first ever function for jarvis startup but i'm modifying into another level, always remembered
def welcome():
#    print("Initializing Jarvis...")
#    print("Love You, 3000")
    print("\n" + "=" * 50)
    print("                 JARVIS MARK I")
    print("=" * 50)
    print("Status        : ONLINE")
    print("Voice Engine  : READY")
    print("Gemini AI     : READY")
    print("Microphone    : READY")
    print("=" * 50)
    print("Love You, 3000 ❤️")



#MISSION 6: CALLING THE FUNCTION.
welcome()


while True:


    #from here we will call command function
    command = takeCommand()

#command normalization
    if command and command.startswith("jarvis"):
        command = command.replace("jarvis", "", 1).strip()



    if command is None:
        continue

    if not execute_command(command):
        break



        

