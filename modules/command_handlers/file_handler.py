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


import os

from modules.speech import say



# ==========================================================
# LAST SEARCH RESULTS
#
# Stores the latest search results temporarily.
# Used for commands like:
#   open 1
#   open 2
# ==========================================================



#------------------------------------------------------------------------------------


# ==========================================================
# GET ALL FILES
#
# Purpose:
# Collect all files from the search locations.
#
# Returns:
# List of full file paths.
# ==========================================================




# ==========================================================
# EXACT FILE SEARCH
# ==========================================================

def search_exact(query, search_paths):

    for folder in search_paths:

        if not os.path.exists(folder):
            continue

        for root, dirs, files in os.walk(folder):

            dirs[:] = [
                d for d in dirs
                if d not in [".venv", ".git", "__pycache__", "node_modules"]
            ]

            for file in files:

                filename = os.path.splitext(file)[0].lower()

                if filename == query.lower():

                    return os.path.join(root, file)

    return None




# ==========================================================
# FUTURE FEATURES
#
# These functions will be implemented in MARK II
# for advanced file searching.
# ==========================================================

# ==========================================================
# STARTS WITH SEARCH
# ==========================================================

def search_startswith(query, search_paths):

    pass


# ==========================================================
# CONTAINS SEARCH
# ==========================================================

def search_contains(query, search_paths):

    pass










def search_file(query):

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

    full_path = search_exact(query, search_paths)


    if full_path:

        filename = os.path.splitext(os.path.basename(full_path))[0]

        say(f"I found {filename}. Opening it, Sir.")

        os.startfile(full_path)

        return

    # ------------------------------------------------------
    # FILE NOT FOUND
    # ------------------------------------------------------

    say("Sorry Sir, I couldn't find that file.")






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