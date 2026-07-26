#mission 24 taking notes by saying anything to jarvis he will note down in note.txt


#importing os 
import os


#creating function
def save_note(note):

    folder = "Notes"

    if not os.path.exists(folder):
        os.makedirs(folder)    

    filepath = os.path.join(folder, "notes.txt")

    with open(filepath, "a") as file:
        file.write(note + "\n")

    return filepath
