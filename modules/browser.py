#brave path much needed for youtube
BRAVE_PATH = r"C:\Users\Harshal\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"


import pywhatkit
import yt_dlp


#MISSION 8: IN THIS WE WILL CALL FUNCTION FROM THIS FILE ie BROWSER.PY
#WE WILL CALL WEBSITES TO OPEN


import webbrowser
import subprocess



#MISSION 9 WE ARE CALLING INDIVIDUAL WEBSITE ie TIME TAKING AND INEFFICIENT


#def open_google():
#    print("Opening Website, Sir..")
#    webbrowser.open("https://www.google.com")

#def open_youtube():
#    print("Opening Website, Sir..")
#    webbrowser.open("https://www.youtube.com")

#def open_github():
#    print("Opening Website, Sir..")
#    webbrowser.open("https://www.github.com")




#MISSION 10 OPENING ANY WEBSITE WHICH IS AVAILABLE IN INTERNET..

def open_website(website):
    print("Opening Site Sir ")
    webbrowser.open("https://www." + website + ".com")


#MISSION 11 SEARCHING IN GOOGLE ANYTHING I WANT NOW..
def search_google(query):
    print("Searching Google for ")
    query = query.replace(" ", "+")
    webbrowser.open("https://www.google.com/search?q=" + query)



#MISSION 12 PLAYING ANY SONG, I WANT NOW..
#MISSION 17 OPENING YOUTUBE VIDEO LINK IN BRAVE SO ADS CAN BE SKIP
#MISSION 18 I HAVE IMPROVED THE YOUTUBE STUFF WHICH IS WAY TOO HARD STILL DIDNT UNDERSTAND THIS BUT SLOWLY I WILL

def play_youtube(song):
    print("Playing The Song...")

    ydl_opts = {
    "quiet": True,
    "no_warnings": True,
    "default_search": "ytsearch1",
}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(song, download=False)

        video_url = info["entries"][0]["webpage_url"]

    subprocess.Popen([BRAVE_PATH, video_url])




#ANOTHER FUNCTION FOR AMAZON SEARCHING
def find_amazon(product):
    print("Searching The Product ")
    product = product.replace(" ", "+")
    webbrowser.open("https://www.amazon.in/s?k=s"+ product)



