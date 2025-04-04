# start sound ke liye hai jo kaam nhinkar rha
from playsound import playsound
import eel

# playing asistant sound function

@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\audio\\notification-18-270129.mp3"
    playsound(music_dir)
    