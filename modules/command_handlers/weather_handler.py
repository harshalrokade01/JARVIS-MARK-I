

from modules.weather import get_weather
from modules.speech import say
from modules.debug import show_hud


def handle_weather_commands(words, command):

    # ------------------------------------------------------
    # WEATHER
    # ------------------------------------------------------

    if words and words[0] == "weather":

        # Agar sirf "weather" bola
        if len(words) < 2:

            say("Please tell me the city name, Sir.")
            return True

        # weather of pune
        if len(words) >= 3 and words[1] == "of":

            city = " ".join(words[2:])

        # weather pune
        else:

            city = " ".join(words[1:])


        result = get_weather(city)

        if result:

            city_name, temperature, humidity, weather = result

            show_hud(
                command=command,
                command_type="WEATHER",
                status="SUCCESS",
                extra=(
                    f"City         : {city_name}\n"
                    f"Temperature  : {temperature:.1f}°C\n"
                    f"Humidity     : {humidity}%\n"
                    f"Weather      : {weather}"
                )
            )
            say(
                f"In {city_name}, the temperature is {temperature} degrees Celsius, "
                f"humidity is {humidity} percent, and the weather is {weather}."
            )


        else:

            say("Sorry Sir, I couldn't find that city.")

        return True

    return None