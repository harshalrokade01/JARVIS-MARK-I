

#HUD FOR JARVIS

def show_hud(command, command_type, status, response_time=None, api_calls=None, extra=None):

    # Command Type Icons
    type_icons = {
        "AI": "🤖 AI",
        "LOCAL": "💻 LOCAL",
        "WEATHER": "🌦️ WEATHER",
        "MEDIA": "🎵 MEDIA",
        "NOTES": "📝 NOTES",
        "SCREENSHOT": "📸 SCREENSHOT"
    }

    # Status Icons
    status_icons = {
        "SUCCESS": "🟢 SUCCESS",
        "FAILED": "🔴 FAILED",
        "PROCESSING": "🟡 PROCESSING"
    }

    command_type = type_icons.get(command_type, command_type)
    status = status_icons.get(status, status)

    print("\n" + "=" * 55)
    print("                ⚡ JARVIS HUD ⚡")
    print("             JARVIS MARK I | v0.1.0")
    print("=" * 55)

    print(f"Command      : {command}")
    print(f"Type         : {command_type}")
    print(f"Status       : {status}")

    if response_time is not None:
        print(f"Response Time: {response_time:.2f} sec")

    if api_calls is not None:
        print(f"API Calls    : {api_calls}")

    if extra is not None:
        print(extra)

    print("=" * 55)

    