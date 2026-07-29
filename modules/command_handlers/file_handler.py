

import os

from modules.speech import say

# ==========================================================
# SEARCH FILE
#
# Purpose:
# Search a file inside the computer.
#
# Returns:
# File Path if found
# None if not found
# ==========================================================

def search_file(query):

    print("search_file() called")
    # ------------------------------------------------------
# IMPORTANT SEARCH LOCATIONS
# ------------------------------------------------------

    search_paths = [

        os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop"),

        os.path.join(os.path.expanduser("~"), "Downloads"),

        os.path.join(os.path.expanduser("~"), "OneDrive", "Documents"),

        os.path.join(os.path.expanduser("~"), "OneDrive", "Pictures"),

        os.path.join(os.path.expanduser("~"), "OneDrive", "Videos"),

    ]

    for folder in search_paths:

        print(f"\nSearching in: {folder}")

        if not os.path.exists(folder):
            continue

        for root, dirs, files in os.walk(folder):

            dirs[:] = [d for d in dirs if d not in [".venv",".git", "__pycache__", "node_modules"]]

            for file in files:

            # ------------------------------------------------------
            # CHECK WHETHER FILE NAME MATCHES USER QUERY
            # ------------------------------------------------------
                filename = os.path.splitext(file)[0].lower()

                if filename == query.lower():

                    full_path = os.path.join(root, file)

                    print(f"Exact Match Found: {file}")

                    os.startfile(full_path)

                    return






# ==========================================================
# FILE COMMAND HANDLER
#
# Purpose:
# Handles searching of files and folders.
#
# Examples:
#   • find resume
#   • find dbms notes
#
# Returns:
#   True  -> Command executed
#   None  -> Command not handled
# ==========================================================

def handle_file_commands(command):

    # ------------------------------------------------------
    # FIND COMMAND (WITHOUT FILE NAME)
    # ------------------------------------------------------

    if command == "find":

        say("What would you like me to find, Sir?")
        return True

    # ------------------------------------------------------
    # FIND FILE COMMAND
    # ------------------------------------------------------

    elif command.startswith("find "):

        query = command.replace("find ", "").strip()

        search_file(query)

        return True

    # Command not handled by File Handler
    return None      