#MISSION 30: ab hum keyboard key ko command through chalayenge example volume high low mute aur bhot kuch

import keyboard

def pause_media():
    keyboard.send("play/pause media")

def next_media():
    keyboard.send("next track")

def previous_media():
    keyboard.send("previous track")

def volume_up():
    keyboard.send("volume up")

def volume_down():
    keyboard.send("volume down")

def mute_volume():
    keyboard.send("volume mute")