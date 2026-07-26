#ye file GEMINI AI (Brain) jo ki jarvis ka brain keh sakte h sab soch aur answer kar sakega
#example: who is elon musk? ya explain bubble sort in java
#just now i downloaded the library python for gemini-ai

#so again and again calling API of GenAi which has limit of 20 only we are now modifying that not everytime jarvis will use ai instead of this only given command will now use the API calling (better API key efficiency...lol)

#--------so here is the brain system gonna work---------
#               Voice
#                 │
#                 ▼
#       Speech Recognition
#                 │
#                 ▼
#        Command Analyzer
#                 │
#     ┌───────────┴───────────┐
#     │                       │
# Local Command?          AI Command?
#     │                       │
#     ▼                       ▼
# Execute Locally        Gemini + Internet
#     │                       │
#     └───────────┬───────────┘
#                 ▼
#               TTS

#Benefit?
#⚡ Local command = Instant
#🌐 AI sirf jab zarurat ho
#💰 API bachegi
#🚀 Faster response



#import karenge new google GENAI SDK ki official library
from google import genai
from google.genai import types


#import load_dotenv jo .env file ko access ya read karega
from dotenv import load_dotenv

#import python built-in module 
import os

import time

api_calls = 0

load_dotenv()

api_key = os.getenv("GEMINI_APIKEY")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"




#creating function
def ask_gemini(prompt):

    global api_calls

#prompt for easy use of gemini
    system_prompt = f"""
You are Jarvis, an AI assistant inspired by Iron Man.

Rules:
- Always reply in English.
- Address the user as "Sir".
- Keep your answers under 40 words.
- Be friendly, professional and confident.
- Never use bullet points unless the user asks.
- Give short and direct answers.

User: {prompt}
"""
    try:
        start = time.time()

        api_calls += 1

#isko modify kar kyuki baar baar galat sunne par program end ho rha
        response = client.models.generate_content(
            model = MODEL_NAME,
            contents=system_prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())]
            )
        )

        end = time.time()

        print(f"API Calls Today: {api_calls}")
        print(f"Gemini Response Time: {end - start:.2f} seconds")

        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")
        return None

#first question and answer given by jarvis to gemini ai (isko comment kr rha hu taaki yaad rhe)
#if __name__ == "__main__":
#    answer = ask_gemini("Who are you?")
#    print(answer)
