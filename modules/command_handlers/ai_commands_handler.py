

from modules.ai import ask_gemini
from modules.speech import say
from modules.debug import show_hud


def handle_ai_commands(command):

    if not command:

        answer, response_time, api_calls = ask_gemini(command)
        
        if answer:
        
            show_hud(
                command=command,
                command_type="AI",
                status="SUCCESS",
                response_time=response_time,
                api_calls=api_calls
            )
        
            print(answer)
            say(answer)
        
        else:
        
            show_hud(
                command=command,
                command_type="AI",
                status="FAILED",
                api_calls=api_calls
            )
        
            say("Sorry Sir, Gemini is unavailable right now. Please try again later.")
        
        return True

    return None

