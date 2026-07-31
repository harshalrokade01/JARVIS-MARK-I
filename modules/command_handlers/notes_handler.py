

from modules.notes import save_note
from modules.speech import say
from modules.debug import show_hud


def handle_notes_commands(command):

    # ------------------------------------------------------
    # SAVE Note
    # ------------------------------------------------------

    if command.startswith(("take note ", "save note ", "make note ")):

        if command.startswith("take note "):
            note = command.replace("take note", "", 1).strip()

        elif command.startswith("save note "):
            note = command.replace("save note", "", 1).strip()

        elif command.startswith("make note "):
            note = command.replace("make note", "", 1).strip()

        filepath = save_note(note)

        say("Note Saved Successfully, Sir.")

        show_hud(
            command=command,
            command_type="NOTES",
            status="SUCCESS",
            extra=f"Saved To: {filepath}"
        )

        return True

    return None