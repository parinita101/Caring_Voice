import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine=pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    engine.setProperty('rate', 174)     # setting up new voice rate
    #print(voices)
    engine.say(text)
    engine.runAndWait()


def takecommand():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('listing...')
        eel.DisplayMessage('listening...')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)

        audio=r.listen(source,10,6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")
        eel.DisplayMessage(query)
        #speak(query)
        eel.ShowHood()
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommand():

    query=takecommand()
    print(query)

    if "start" in query:
        print("I start")
    else:
        print("not")

#text=takecommand()

'''
speak(text)

speak("hello pari. how are you?")'''