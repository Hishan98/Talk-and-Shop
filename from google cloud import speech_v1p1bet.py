import playsound
from gtts import gTTS

def speak(text):
        tts = gTTS(text=text, lang='en-uk')
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
speak("Hi Guys")