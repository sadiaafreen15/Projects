import speech_recognition as sr 
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("how do you feel?")
    speak("how do you feel?")
    audio=r.listen(source,timeout=15,phrase_time_limit=10)
    print("ok")

try:
    print("Text to speech:"+r.recognize_google(audio))
except:
    pass;
from textblob import TextBlob
blob=TextBlob(" "+ r.recognize_google(audio))
x=blob.sentiment.polarity

if x<0:
    speak('you look sad dont worry, you will be fine')
    print('you look sad dont worry, you will be fine')
elif x==0:
    speak('thats alright')
    print('thats alright')
elif x>0:
    speak('you look happy so glad to hear this')
    print('you look happy so glad to hear this')
elif x<=1:
    speak('you look happy so glad to hear this')
    print('you look happy glad to hear this')




