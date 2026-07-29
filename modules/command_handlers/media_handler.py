

from modules.media import *

def handle_media_commands(command):

    # ------------------------------------------------------
    # PAUSE / RESUME MEDIA
    # ------------------------------------------------------

    if command in ["pause", "resume", "play", "pause music", "resume music"]:

        pause_media()

        return True

    # ------------------------------------------------------
    # NEXT MEDIA
    # ------------------------------------------------------

    elif command in ["next", "next song", "next music"]:

        next_media()

        return True


    # ------------------------------------------------------
    # PREVIOUS MEDIA
    # ------------------------------------------------------

    elif command in ["previous", "previous song", "previous music"]:

        previous_media()

        return True


    # ------------------------------------------------------
    # VOLUME UP
    # ------------------------------------------------------

    elif command in ["volume up", "increase volume"]:

        volume_up()

        return True


    # ------------------------------------------------------
    # VOLUME DOWN
    # ------------------------------------------------------

    elif command in ["volume down", "decrease volume"]:

        volume_down()

        return True


    # ------------------------------------------------------
    # MUTE VOLUME
    # ------------------------------------------------------

    elif command in ["mute", "unmute", "mute volume", "unmute volume"]:

        mute_volume()

        return True


    return None