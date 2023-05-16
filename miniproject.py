from cgitb import text
from email.mime import audio
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
from newsapi import NewsApiClient
import sys
import random
import requests
from urllib.request import urlopen
import json
import config
from GoogleNews import GoogleNews
from textblob import TextBlob
from email.message import EmailMessage
import smtplib
import yagmail
import wolframalpha
from googletrans import Translator




sys.path.append('/usr/local/lib/python3.7/dist-packages/')

import pyjokes
#import pywhatkit as pwk



newsapi = NewsApiClient(api_key='API_KEY')
googlenews=GoogleNews()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")   

    else:
        speak("Good Evening!")  
        print("Good Evening!")

    speak("May I know your name Human?") 
    name=takeCommand()      
    speak('nice to meet you'+name)
    speak('I am Jarvis, your virtual assistant. How may I help you?')


    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=5)
        r.adjust_for_ambient_noise(source, duration=1)
        
    try:
        print('Recognizing...')    
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")


    except Exception as e:
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query

class WeatherService(object):

    API_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric";

    API_KEY = "3b31a7e394e41c3a30759dfde1a3383e";

    def __init__(self):
        pass

   

def weather():
        city = "hyderabad"
        res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
        temp1 = res["weather"][0]["description"]
        temp2 = res["main"]["temp"]
    
        speak(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")



def get_random_advice():
        results = requests.get("https://api.adviceslip.com/advice").json()
        return results['slip']['advice']
 

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:

            speak("I am good, how are you?")
            print("i am good")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            
            path='C:\\Users\\DELL\\OneDrive\\Desktop\\jarvis.py\\audios'
            files=os.listdir(path)
            d=random.choice(files)
            os.startfile(f"C:\\Users\\DELL\\OneDrive\\Desktop\\jarvis.py\\audios\\{d}")
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'repeat after me' in query:
            speak("what do you want me to say")
            sentence=takeCommand()
            speak("hmm"+sentence)

        elif "where is" in query:
         
            listening = True
            query = query.split(" ")
            location_url = "https://www.google.com/maps/place/" + str(query[2])
            speak("Hold on, I will show you where " + query[2] + " is.")
            webbrowser.open(location_url)

        
        elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

        
        elif 'song' in query:
                
            song = query.replace('play ', '')
            speak('playing ' + song)
            pwk.playonyt("ami je tomar song", use_api=False)

        elif "advice" in query:
            speak(f"Here's an advice for you all")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)

        elif ('weather' in query):
            weather()
            

        
        elif 'whatsapp' in query:
            try:
            # sending message to receiver--
            # using pywhatkit
                pwk.sendwhatmsg("+917702515798","Hello, Jarvis here",22, 48)
                print("All Messages Sent")
            except:
                print("An Unexpected Error!")
        


        elif "calculate" in query:
             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

      
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
 
       
           

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
            results=pyjokes.summary(query,sentences=3)
            print(results)

        elif 'who is the best' in query:
            speak("undoubtedly, Sadia is the best")
        
        elif 'text' in query:
            speak('hi sir. sadia asked me to check on you? how do you feel?')

        elif 'how are you' in query:
            speak("I am good, how are you?")

        elif 'news' in query:
            news = webbrowser.open_new_tab ('https://timesofindia.indiatimes.com/home/headlines')
            speak(news)
# Specify the query and number of returns')
            speak('Here are some headlines from the Times of India,Happy reading')
          
           
        elif 'whatsapp' in query:
            try:
      # sending message in Whatsapp in India so using Indian dial code (+91)
                pwk.sendwhatmsg("+917386978652", "Hi sir, we share a common boss", 2, 13)
 
                print("Message Sent!") #Prints success message in console
 
     # error message
            except: 
                print("Error in sending the message")

        elif 'headlines' in query:
            speak('Getting news for you...')
            engine.runAndWait()
            googlenews.get_news('Todays news')
            googlenews.result()
            results=googlenews.gettext()
            print(*results[8:15],sep=',')
            speak(results[8:16])

          
        elif 'sentiment' in query:
     
            r = sr.Recognizer()
            with sr.Microphone() as source:      
                print("how do you feel?")
                speak("how do you feel?")
                audio=r.listen(source,timeout=15,phrase_time_limit=5)
                print("ok")

            try:
                print("Text to speech:"+r.recognize_google(audio))
            except:
                pass;
         
            from textblob import TextBlob
            r = sr.Recognizer()
    
            blob=TextBlob(" " +r.recognize_google(audio))
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


def takeCommandHindi():
         
    r = sr.Recognizer()
    with sr.Microphone() as source:
          
        # seconds of non-speaking audio before 
        # a phrase is considered complete
        print('Listening')
        r.pause_threshold = 0.7  
        audio = r.listen(source)  
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='hi-In')
              
            # for listening the command in indian english
            print("the query is printed='", Query, "'")
          
        # handling the exception, so that assistant can 
        # ask for telling again the command
        except Exception as e:
            print(e)  
            print("Say that again sir")
            return "None"
        return Query
  
  
  
# Driver Code
           
# call the function
takeCommandHindi()