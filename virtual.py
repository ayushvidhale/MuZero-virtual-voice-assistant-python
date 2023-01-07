from matplotlib.pyplot import close
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import pywhatkit
import requests
import pyjokes
import cv2 as cv
import pyautogui
import random

import webbrowser, urllib, re
import urllib.parse
import urllib.request


GREETINGS = ["hello Muzero", "Muzero", "wake up Muzero", "you there Muzero", "time to work Muzero", "hey Muzero",
             "ok Muzero", "are you there"]

GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]
#All Files Code here :

# 1. Youtube
def youtube():

    # domain = input("Enter the song name: ")
    domain = statement
    song = urllib.parse.urlencode({"search_query" : domain})
    print("Song" + song)

    # fetch the ?v=query_string
    result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
    print(result)

    # make the url of the first result song
    search_results = re.findall(r'href=\"\/watch\?v=(.{4})', result.read().decode())
    print(search_results)

    # make the final url of song selects the very first result from youtube result
    url = "http://www.youtube.com/watch?v="+str(search_results)

    # play the song using webBrowser module which opens the browser 
    # webbrowser.open(url, new = 1)
    webbrowser.open_new(url)


print('Starting your AI personal assistant - MuZero')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant MuZero")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant MuZero is shutting down,Good bye')
            print('your personal assistant MuZero is shutting down,Good bye')
            break


        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        # elif re.search('open', statement):
        #         domain = statement.split(' ')[-1]
        #         open_result = obj.website_opener(domain)
        #         speak(f'Alright sir !! Opening {domain}')
        #         print(open_result)

        elif 'youtube' in statement:
                youtube()
                video = statement.split(' ')[1]
                speak(f"Okay sir, playing {video} on youtube")
                pywhatkit.playonyt(video)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif "play music" in statement or "hit some music" in statement:
                music_dir = "F://Songs//Imagine_Dragons"
                songs = os.listdir(music_dir)
                for song in songs:
                    os.startfile(os.path.join(music_dir, song))

        # elif "what do i have" in statement or "do i have plans" or "am i busy" in statement:
        #         obj.google_calendar_events(command)
        #         def note(text):
        #             date = datetime.datetime.now()
        #             file_name = str(date).replace(":", "-") + "-note.txt"
        #             with open(file_name, "w") as f:
        #                 f.write(text)
        #             notepad = "C://Program Files (x86)//Notepad++//notepad++.exe"
        #             subprocess.Popen([notepad, file_name])
        #         note(statement)

        elif "joke" in statement:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

        elif 'Gmail' in statement:
            print("Gmail was used")
            webbrowser.open_new_tab("https://www.gmail.google.com")
            speak("Google Mail is opened now for you")
            time.sleep(5)

        elif "switch the window" in statement or "switch window" in statement or "switch tab" in statement:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

        elif "take screenshot" in statement or "take a screenshot" in statement or "capture the screen" in statement:
                speak("By what name do you want to save the screenshot?")
                # name = obj.mic_input()
                name = statement
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")


        elif "ip address" in statement:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak("City Not Found ")


        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif statement in GREETINGS:
                speak(random.choice(GREETINGS_RES))

        elif 'who are you' in statement or 'what can you do' in statement or 'something about yourself' in statement:
            speak('I am Muzero version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Chiku")
            print("I was built by Chiku")

        elif "open stackoverflow" in statement or "stack" in statement  or "overflow" in statement :
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            # ec.capture(0,"robo camera","img.jpg")
            cam = cv.VideoCapture(0)   
            s, img = cam.read()
            if s:
                cv.namedWindow("cam-test")
                cv.imshow("cam-test",img)
                cv.waitKey(0)
                cv.destroyWindow("cam-test")
                cv.imwrite("filename.jpg",img)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "hide all files" in statement or "hide this folder" in statement:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden")

        elif "visible" in statement or "make files visible" in statement:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")


        elif "goodbye" in statement or "offline" in statement or "bye" in statement:
                speak("Alright sir, going offline. It was nice working with you")
                exit()

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])


time.sleep(3)
