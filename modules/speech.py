#MISSION 13 MAKING JARVIS TO SPEAK BY USING LIBRARY LIKE EDGE_TTS AND ASYNCI

import edge_tts
import asyncio
import tempfile

from modules.config import VOICE, SPEECH_RATE

#to import audio file we use import os
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame

#pygame.mixer.init()

#improving tts command responser ie reducing time delay
async def speak(text):

    if not pygame.mixer.get_init():
        pygame.mixer.init()


    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_path = temp_file.name

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate=SPEECH_RATE
    )    
    await communicate.save(temp_path)

    pygame.mixer.music.load(temp_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()

    os.remove(temp_path)

def say(text):
    asyncio.run(speak(text))