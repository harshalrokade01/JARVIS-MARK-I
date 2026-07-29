

from modules.browser import *

def handle_browser_commands(words, command):

    # ------------------------------------------------------
    # OPEN GOOGLE
    # ------------------------------------------------------

    if command == "open google":

        open_website("google")

        return True

    # ------------------------------------------------------
    # OPEN YOUTUBE
    # ------------------------------------------------------

    elif command == "open youtube":

        open_website("youtube")

        return True

    # ------------------------------------------------------
    # SEARCH GOOGLE
    # ------------------------------------------------------

    elif command.startswith("search "):

        query = command.replace("search", "", 1).strip()

        search_google(query)

        return True


    # ------------------------------------------------------
    # PLAY YOUTUBE
    # ------------------------------------------------------

    elif command.startswith("play "):

        song = command.replace("play", "", 1).strip()

        play_youtube(song)

        return True


    # ------------------------------------------------------
    # SEARCH AMAZON
    # ------------------------------------------------------

    elif command.startswith("amazon ", "buy ", "by "):

        product = command

    product = command

    if command.startswith("amazon "):

        product = command.replace("amazon", "", 1).strip()

    elif command.startswith("buy "):

        product = command.replace("buy", "", 1).strip()


    find_amazon(product)

    return True

        








    return None