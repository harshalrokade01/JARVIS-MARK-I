#MISSION 13 MAKING JARVIS TO SPEAK BY USING LIBRARY LIKE EDGE_TTS AND ASYNCI

import edge_tts
import asyncio
import tempfile

#to import audio file we use import os
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame

pygame.mixer.init()

#improving tts command responser ie reducing time delay
async def speak(text):


    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_path = temp_file.name

    communicate = edge_tts.Communicate(text, "en-IN-PrabhatNeural")
    await communicate.save(temp_path)

#    tts_end = time.time()
#    print(f"TTS Generation: {tts_end - start:.2f} seconds")

    pygame.mixer.music.load(temp_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()

#    play_end = time.time()
#    print(f"Audio Playback: {play_end - tts_end:.2f} seconds")

    os.remove(temp_path)

def say(text):
    asyncio.run(speak(text))