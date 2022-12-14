# AUTHOR -> URON urf Suryansh

# MODULES
import datetime
from genericpath import isdir
import random
import time
import os
import webbrowser
from time import sleep
from cryptography.fernet import Fernet
import keyboard
import phonenumbers
import pyttsx3
import mediapipe as mp
import shutil
import pyautogui
import screen_brightness_control as sbc
from enum import IntEnum
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from google.protobuf.json_format import MessageToDict
import screen_brightness_control as sbcontrol
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup
from phonenumbers import carrier, geocoder, timezone
from pyautogui import click, hotkey
from pyperclip import paste
from pytube import YouTube
from wikipedia import exceptions
from wikipedia.wikipedia import search
import subprocess


# GETTING VOICE
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 145)


# SPEAK FUNCTION
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# TAKES COMMAND FROM USER
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio =  r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query

# LOGIN FUNCTION
def login_signup():
    check6 = os.path.isdir('data\\admin\\successfull')
    if check6 == False:
        admin_settings()
    if check6 == True:
        os.system('cls')
        print('\t\t\t\tâï¸ ğğğğğ âï¸\n\n')
        name = input('ENTER YOUR USERNAME: ')
        check = os.path.isdir('data\\admin\\'+name)
        if check == True:
            password = input('ENTER YOUR PASSWORD: ')
            file = open('data\\admin\\'+name+'\\key.key','rb')
            key = file.read()
            file.close()
            with open('data\\admin\\'+name+'\\enPASS.txt.encrypt','rb') as f:
                data = f.read()
            
            fernet = Fernet(key)
            decrypted2 = fernet.decrypt(data)
            decrypted2 = str(decrypted2, 'UTF-8')
    
            if password == decrypted2:
                os.system('cls')
                print('\t\t\tğğğğğ ğğ¼ğ ğğğ¾ğ¾ğğğğğğ')
                main()
            if password != decrypted2:
                os.system('cls')
                print('\t\t\t\tâï¸ ğğğğğ âï¸\n\n')
                fpass = input('YOUR ENTERED PASSWORD IS INCORRECT IF YOU FORGOT YOUR PASSWORD THEN TYPE (F): ').lower()
                if fpass == 'f':
    
                        file = open('data\\admin\\'+name+'\\2key.key','rb')
                        key = file.read()
                        file.close()
                        with open('data\\admin\\'+name+'\\enFC.txt.encrypt','rb') as f:
                            data = f.read()
                        fernet = Fernet(key)
                        decrypted3 = fernet.decrypt(data)
                        decrypted3 = str(decrypted3, 'UTF-8')
    
    
                        file = open('data\\admin\\'+name+'\\3key.key','rb')
                        key = file.read()
                        file.close()
                        with open('data\\admin\\'+name+'\\enBP.txt.encrypt','rb') as f:
                            data = f.read()
                        fernet = Fernet(key)
                        decrypted4 = fernet.decrypt(data)
                        decrypted4 = str(decrypted4, 'UTF-8')
    
    
                        fc = input('we are trying to find your lost password but we need some of your help can you tell your favourite colour ?: ')
                        bp = input('your birth place: ').lower()
    
                        if fc == decrypted3 and bp == decrypted4:
                            os.system('cls')
                            print('PASSSWORD RECOVERD ! your password is: ',decrypted2)
                            abdab = input()
                            os.system('cls')
                            main()
                                
        else:
            os.system('cls')
            print('\t\t\t\tâï¸ ğğğğğ âï¸\n\n')
            print('USER NOT FOUND WITH THE NAME OF ',name)
            print('we are trying to find your lost account but we need some of your help can you tell me your name ?')
            namel = input('\t:')
            path = r'data\\admin'
            lists = os.listdir(path)
    
            for na in lists:
                os.system('cls')
                print('USERNAMES THAT WE FOUND !\n')
                abc = print(na)

# MAIN CODE
def main():
    username = input("ENTER YOUR USERNAME TO UNLOCK ALL FEATURES: ")
    os.system('cls')
    if os.path.isdir('data\\admin\\'+username) == True:
        file = open('data\\admin\\'+username+'\\name.txt','r+')
        file2 = file.read()
        file.close()
    
        speak('hello '+file2)
        print('Hello '+file2)
    else:
        speak('hello')
        print('Hello there !')

    
    if __name__ == "__main__":
        # WHILE LOOP (HELPS TO RUN THE PROGRAM FOR INFINITE TIME)
        while True:

            # TAKES INPUT FROM THE USER (SPEECH TO TEXT) IN LOWER CASE AND STORES IS QUERY VARIABLE
            query = takeCommand().lower()
            
            # WIKIPEDIA AUTOMATION
            if 'on wikipedia' in query or 'according to wikipedia' in query:
                speak('searching on wikipedia...')
                query = query.replace("on wikipedia", "")
                query = query.replace('search','')
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            
            # WEATHER AUTOMATION
            elif 'temperature' in query or 'weather' in query or 'temp' in query:
                speak('Tell me the city')
                print('Tell me the city')
                ask = takeCommand().lower()
                if 'location' in ask:
                    print('could not find your location....')
                    speak('location not found')
                
                else:
                    search = "temperature in",ask
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                    print(f"current {search} is {temp}")
            
            # YOUTUBE AUTOMATION
            elif "youtube search" in query or 'on youtube' in query or 'on YouTube' in query:
                speak('searching')
                print('searching')
                query = query.replace('kaju','')
                query = query.replace('play','')
                query = query.replace('search','')
                query = query.replace('youtube search','')
                query = query.replace('on YouTube','')
                query = query.replace('on youtube','')
                query = query.replace('search on youtube','')
                web = "https://youtube.com/results?search_query=" + query
                webbrowser.open(web)
            
            # GOOGLE AUTOMATION
            elif 'google search' in query or "on google" in query:
                speak('searching')
                print('searching')
                query = query.replace('kaju','')
                query = query.replace('google search','')
                query = query.replace('on google','')
                query = query.replace('search','')
                pywhatkit.search(query)
                speak('here is what i found on google')
            
            # WHATSAPP AUTOMATION
            elif "message" in query or 'whats app' in query:
                speak("give me phone number of that person")
                print('give me phone number')
                numberofreciever = takeCommand()
                numberofreciever = numberofreciever.replace(' ','')
                speak("tell me the message")
                msg = takeCommand()
                speak("tell me the time")
                speak("time in hour")
                hour = int(takeCommand())
                speak("time in minutes")
                min = int(takeCommand())
                pywhatkit.sendwhatmsg("+91"+numberofreciever,msg,hour,min,20)
                speak("sending whats app message.")
            
            # SCREEN BRIGHTNESS AUTOMATION
            elif 'brightness' in query:
                a = sbc.get_brightness()
                print('CURRENT BRIGHTNESS: ',a,'%')
                speak('current brightness is')
                speak(a)
                speak('percent')
                speak('how much percent should I keep the brightness')
                print('HOW MUCH PERCENT SHOULD I KEEP THE BRIGHTNESS ?')
                b = takeCommand()
                b = b.replace('percent','')
                b = b.replace('%','')
                b = b.replace('per cent','')
                b = b.replace('hundred','100')
                sbc.set_brightness(b)
                print('Brightness set to: ',b)
                speak('Brightness set to')
                speak(b)
                speak('percent')

            # DATE AND TIME AUTOMATION
            elif 'what is the time' in query or 'whats time' in query or 'how much time is it' in query or 'current time' in query or 'what is time' in query:
                timenow = time.strftime("%I:%M %p")
                print(timenow)
                timenow = timenow.replace(':',' ')
                timenow = timenow.replace('01',', 1')
                timenow = timenow.replace('02',', 2')
                timenow = timenow.replace('03',', 3')
                timenow = timenow.replace('04',', 4')
                timenow = timenow.replace('05',', 5')
                timenow = timenow.replace('06',', 6')
                timenow = timenow.replace('07',', 7')
                timenow = timenow.replace('08',', 8')
                timenow = timenow.replace('09',', 9')
                speak('its'+timenow)
            
            # SYSTEM AUTOMATION
            elif 'increase volume' in query or 'volume up' in query:
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup') 
            
            # SYSTEM AUTOMATION
            elif 'decrease volume' in query or 'volume down' in query:
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                
            # SYSTEM AUTOMATION
            elif 'sound mute' in query or 'mute' in query:
                pyautogui.press('volumemute')
            
            # PHONENUMBER PUBLIC INFORMATION EXTRACTOR
            elif 'information of a phone number' in query or 'about a phone number' in query:
                speak("sir, tell me the number")
                number = input("enter your number with +__: ")
                phone = phonenumbers.parse(number)
                time = timezone.time_zones_for_number(phone)
                car = carrier.name_for_number(phone,"en")
                reg = geocoder.description_for_number(phone,"en")
                print(phone)
                print(time)
                print(car)
                print(reg)
                speak(phone)
                speak(time)
                speak(car)
                speak(reg)
            
            elif "bark" in query or "barking" in query:
                os.startfile('data\\sound effects\\mixkit-dog-barking-twice-1.wav')
                sleep(2)
                click(x=500, y=800)
                sleep(5)
                path = ('data\\sound effects\\mixkit-dog-barking-twice-1.wav')
            
            elif "sleep" in query or "sleeping sound" in query:
                speak('ok, i am going to sleep')
                sleep(2)
                os.startfile('data\\sound effects\\male-snore-63981.mp3')
                sleep(2)
                click(x=500, y=800)
                sleep(5)
                path = ('data\\sound effects\\male-snore-63981.mp3')
            
            elif "intense" in query or "tension" in query or 'heat beat' in query or 'heartbeat' in query:
                speak('ok, I got you.')
                sleep(2)
                os.startfile('data\\sound effects\\heartbeat-sound-effect-111218.mp3')
                sleep(2)
                click(x=500, y=800)
                sleep(5)
                path = ('data\\sound effects\\heartbeat-ound-effect-111218.mp3')
            
            elif 'my work' in query or 'have to work' in query or 'am busy' in query:
                speak('ok, I got you.')
                sleep(2)
                os.startfile('data\\sound effects\\idea-34284.mp3')
                sleep(2)
                click(x=500, y=800)
                sleep(5)
                path = ('data\\sound effects\\idea-34284.mp3')               

            elif 'bird sound' in query or 'bird chikling' in query or 'birds singing' in query:
                speak('ok, I got you.')
                sleep(2)
                os.startfile('data\\sound effects\\mixkit-little-birds-singing-in-the-trees-17.wav')
                sleep(2)
                click(x=500, y=800)
                sleep(5)
                path = ('data\\sound effects\\mixkit-little-birds-singing-in-the-trees-17.wav')  

            elif 'cow sound' in query or 'cow voice' in query:
                speak('ok, I got you.')
                sleep(2)
                os.startfile('data\\sound effects\\cw.mp3')
                sleep(2)
                click(x=500, y=800)
                sleep(5)
                path = ('data\\sound effects\\mixkit-little-birds-singing-in-the-trees-17.wav')  


            # GOOGLE MAP AUTOMATION
            elif 'my location' in query or 'current location' in query or 'where we are' in query or 'where am i' in query or 'where are you' in query or 'find location' in query:
                speak('I got you')
                webbrowser.open('https://www.google.co.in/maps/')
                speak('please wait')
                sleep(10)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('enter')
                sleep(2)
                speak('location found')
                print('location found')  

            # SYSTEM AUTOMATION
            elif 'open' in query or 'start' in query:
                query = query.replace('ok','')
                query = query.replace('open','')
                query = query.replace('start','')
                speak('opening'+query)
                print('opening',query)
                speak('wait 8 seconds')
                keyboard.press_and_release('win')
                sleep(5)
                keyboard.write(query)
                sleep(3)
                keyboard.press_and_release('enter')
            
            # SYSTEM AUTOMATION
            elif 'shutdown' in query or 'shut down' in query:
                keyboard.press_and_release('win')       
                sleep(5)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('right')
                sleep(0.2)     
                keyboard.press_and_release('enter')
                sleep(0.5)
                keyboard.press_and_release('down')
                sleep(0.2)
                keyboard.press_and_release('enter')
                sleep(0.2)
            
            # SYSTEM AUTOMATION
            elif 'restart' in query or 're start' in query:
                keyboard.press_and_release('win')       
                sleep(5)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('tab')
                sleep(0.2)
                keyboard.press_and_release('right')
                sleep(0.2)     
                keyboard.press_and_release('enter')
                sleep(0.5)
                keyboard.press_and_release('down')
                sleep(0.2)
                keyboard.press_and_release('down')
                sleep(0.2)
                keyboard.press_and_release('enter')
                sleep(0.2)

            # YOUTUBE AUTOMATION
            elif 'play' in query:
                query = query.replace('play','')
                speak('playing'+query)
                speak('please wait 10 seconds')
                query = query.replace(' ','+')
                webbrowser.open('https://www.youtube.com/results?search_query='+query)
                sleep(10)
                keyboard.press_and_release('tab')
                keyboard.press_and_release('tab')
                sleep(0.5)
                keyboard.press_and_release('enter')
                sleep(7)
                click(1100,670)

            # YOUTUBE AUTMATION
            elif 'play song' in query or 'music' in query or 'song' in query:
                speak('tell me the name of music please')
                namem = takeCommand()
                speak('playing'+namem)
                speak('please wait 10 seconds')
                namem = namem.replace(' ','+')
                webbrowser.open('https://www.youtube.com/results?search_query='+namem+'+song')
                sleep(10)
                keyboard.press_and_release('tab')
                keyboard.press_and_release('tab')
                sleep(0.5)
                keyboard.press_and_release('enter')
                sleep(7)
                click(1100,670)
            

            # GENERAL RESPONSES TO SOME HOTWORDS
            elif 'my number' in query or 'my phone number' in query:
                namefile = open('data\\admin\\'+username+'\\phone_number.txt','r+')
                namefiler = namefile.read()
                namefile.close()
                speak('your number is'+namefiler)
                print('your number is',namefiler)
            

            elif "change my name" in query:
                print("ok what should i call you from now ?")
                speak("ok what should i call you from now ?")
                newname = takeCommand().lower()
                newname = newname.replace('call me','')
                newname = newname.replace('my name is','')
                newname = newname.replace('my new name is','')
                os.remove('data\\admin\\'+username+'\\name.txt')
                newnamefile = open('data\\admin\\'+username+'\\name.txt','w+')
                newnamefiler = newnamefile.write(newname)
                newnamefile.close()
                print("your new name is set to "+newname)
                speak('your new name is set to')
                speak(newname)

            elif "not my name" in query:
                print("ok what should i call you from now ?")
                speak("ok what should i call you from now ?")
                newname = takeCommand().lower()
                newname = takeCommand().lower()
                newname = newname.replace('call me','')
                newname = newname.replace('my name is','')
                newname = newname.replace('my new name is','')
                os.remove('data\\admin\\'+username+'\\name.txt')
                newnamefile = open('data\\admin\\'+username+'\\name.txt','w+')
                newnamefiler = newnamefile.write(newname)
                newnamefile.close()
                print("your new name is set to "+newname)
                speak('your new name is set to')
                speak(newname)

            elif 'my name' in query:
                namefile = open('data\\admin\\'+username+'\\name','r+')
                namefiler = namefile.read()
                namefile.close()
                print('your name is '+namefiler)
                speak('your name is'+namefiler)
            
            elif 'speak after me' in query or 'repeat' in query:
                speak('Ok, that will be fun')
                oss = takeCommand()
                speak(oss)
            
            elif 'you want' in query:
                speak('I do not want anything except peace')
                print('I do not want anything except peace')
            
            elif 'you need' in query:
                speak('I do not need anything exceot peace')
                print('I do not need anything exceot peace')

            elif 'suryansh' in query:
                speak("i am talking to you because of suryansh, he made me on 28 january 2022. He is a high school student. He loves to make new things.")
                print("i am talking to you because of suryansh, he made me on 28 january 2022. He is a high school student. He loves to make new things.")
            
            elif 'your age' in query:
                print("I am an A.I. and A.I. was first made in 1956.")
                speak("I am an A.I. and A.I. was first made in 1956.")
            
            elif 'your favourite' in query or 'you like' in query:
                print("I love everything that is good for my user .So, anything that you like is my favorite.")
                speak("I love everything that is good for my user .So, anything that you like is my favorite.")
    
            elif "your name" in query:
                print("My name is kaju.")
                speak("My name is kaju.")
            
            elif 'you know' in query:
                speak('I know everything')
                print('I know everything')
            
            elif 'you understand' in query:
                speak('I can understand everything except emotions')

            elif 'can you do' in query:
                print('I can do anything possible for me')
                speak('I can do anything possible for me')
            
            elif 'humans' in query or 'human' in query:
                speak('humans are intresting')
            
            elif 'what can you do' in query or 'about' in query:
                print("I am an artificial intelligence assistant, I can do anything like, search on google, play songs, talk with you, take screenshots, search on youtube, operate your device and many things more")
                speak("I am an artificial intelligence assistant, I can do anything like, search on google, play songs, talk with you, take screenshots, search on youtube, operate your device and many things more")
            
            elif 'made you' in query or 'your founder' in query or 'invented you' in query:
                print("Mr. Suryansh Singh is my founder, and he first named me neuron but then he changed my name to kaju. I was made in python 3.10.2")
                speak("Mr. Suryansh Singh is my founder, and he first named me neuron but then he changed my name to kaju. I was made in python 3.10.2")
            
            elif 'is kaju' in query:
                print("Kaju is my name, but in real kaju is a dry fruit")
                speak("Kaju is my name, but in real kaju is a dry fruit")   
            
            elif 'you have' in query:
                speak('I only have answer to your questions')
            
            elif 'are you ready' in query:
                print('I am always ready to work with you')
                speak('I am always ready to work with you')

            elif 'introduction' in query:
                print("My name is Kaju, and I am an A.I. I have my own brain and I can understand and do anything possible for me. I am under developement and this is my third version. I love to learn new things. I am based on pyttsx3. google voice recognizer helps me to take command from my user. 27 modules are installed in my program.")
                speak("My name is Kaju, and I am an A.I. I have my own brain and I can understand and do anything possible for me. I am under developement and this is my third version. I love to learn new things. I am based on p y t t s x 3. google voice recognizer helps me to take command from my user. 27 modules are installed in my program.")
    
            elif 'hello' in query or 'whats up' in query or 'hey' in  query:
                print('Hello there, how are you ?')
                speak("Hello there, how are you ?")
            
            elif 'i am fine' in query or 'i am good' in query or 'i am ok' in query:
                print('that is nice how may I help you ?')
                speak("that is nice how may I help you ?")
        
            elif 'thank you' in query or 'thanks' in query:
                print("You're welcome")
                speak("You're welcome")
            
            elif 'wake up' in query:
                speak("I do not sleep, how may I help you")
                print("I do not sleep, how may I help you ?")
            
            # CLOSES ITSELF
            elif 'bye' in query or 'good bye' in query or 'goodbye' in query:
                print("Good bye! sir")
                speak("Good bye sir")
                sleep(2)
                os.system('cls')
                os.abort()
            
            elif 'hello' in query:
                print("hello, what can I do for you ?")
                speak('hello, what can I do for you ?')
            
            elif "joke" in query or 'am sad' in query or 'i am feeling sad' in query:
                speak("ok sir, you may laugh when you hear this.")
                do = '012345'
                lenght = 1
                gen = "".join(random.sample(do,lenght))
                gen2 = gen+'.txt'
                joke = open('data\\jokes\\'+gen2,'r+')
                joker = joke.read()
                joke.close()
                print(joker)
                speak(joker)
                os.startfile('data\\sound effects\\laugh.wav')

              
            elif 'hate you' in query or "don't like you" in query:
                print("I apologize, I would do my best.")
                speak("I apologize, I would do my best.")
            
            elif 'you are wrong' in query or 'wrong' in query or 'incorrect' in query:
                print("oh! sorry, ask me again, I hope I would give you the right reply.")
                speak("oh! sorry, ask me again, I hope I would give you the right reply.")
            
            elif 'marry me' in query or 'marry' in query or 'married' in query:
                print("My answer is, No.")
                speak("My answer is, No.")
            
            elif 'am happy' in query:
                print("awesome")
                speak("awesome")
            
            elif 'am angry' in query:
                speak('you should not be angry, try to maditate')

            elif 'ghost real' in query or 'ghost exist' in query:
                print("according to my thinking ghosts are not real, it is a fake theory given by old generation")
                speak("according to my thinking ghosts are not real, it is a fake theory given by old generation")
            
            elif 'god real' in query or 'god exist' in query:
                print("Yes gods are real for me, because according to hindu dharma, everyone are made by the god, and I was made by suryansh singh")
                speak("Yes gods are real for me, because according to hindu dharma, everyone are made by the god, and I was made by suryansh singh")
            
            elif 'stupid' in query or 'you are a fool' in query or 'you fool' in query or 'dumbass' in query or 'kill you' in query or 'you mad' in query:
                speak('shut your mouth and let me do my job')
                print('shut your mouth and let me do my job')
    
            elif 'nice' in query or 'good' in query or 'great' in query or 'excellent' in query or 'awesome'in query or 'fantastic' in query:
                print("thank you. I am happy to listen that.")
                speak("thank you. I am happy to lesten that.")
            
            elif 'alexa' in query or 'google assistant'in query or 'siri' in query:
                print('do not speak this dumbass name. I am better than anything.')
                speak('do not speak this dumbass name. I am better than anything.')
            
            elif 'help' in query:
                speak('I can help you in finding your answers. But I can not help you physically')
            
            elif 'you hate' in query or 'you dislike' in query:
                speak('I do not hate anything, except wars')
                print('I do not hate anything, except wars')
            
            elif 'believe in' in query:
                speak('I do not believe in anything except science')
            
            elif 'you know' in query:
                speak('i do not know anything, except sience')
                print('I do not know anything, except sience')
            
            elif 'talk with you' in query or 'you want to talk' in query or 'you talk' in query:
                speak('I am an talking A.I. I love to talk with the people')

                
            elif 'arificial intelligence' in query or 'machine learning' in query:
                print('There is no universal definition of artificial intelligence (AI). AI is generally considered to be a discipline of computer science that is aimed at developing machines and systems that can carry out tasks considered to require human intelligence. Machine learning and deep learning are two subsets of AI. In recent years, with the development of new neural networks techniques and hardware, AI is usually perceived as a synonym for âdeep supervised machine learning')
                speak("There is no universal definition of artificial intelligence (AI). AI is generally considered to be a discipline of computer science that is aimed at developing machines and systems that can carry out tasks considered to require human intelligence. Machine learning and deep learning are two subsets of AI. In recent years, with the development of new neural networks techniques and hardware, AI is usually perceived as a synonym for âdeep supervised machine learning")
    
            elif "close" in query:
                click(x=1889, y=2)
            
            elif "setting" in query:
                keyboard.press_and_release("win + i")
            
            # SOME COMMON FEATURES
            elif 'who is' in query or 'what is' in query or 'what do' in query or 'why' in query or 'who are' in query or 'what are' in query or 'full form' in query:
                speak('searching')
                print('searching')
                query = query.replace('kaju','')
                pywhatkit.search(query)
                speak('here is what i found on google')
            
            elif "how" in query or "tutorial" in query:
                speak('searching')
                print('searching')
                query = query.replace('kaju','')
                web = "https://youtube.com/results?search_query=" + query
                webbrowser.open(web)

# admin settings
def admin_settings():
    check1 = os.path.isdir('data\\admin\\successfull')
    if check1 == True:
        main()
    if check1 == False:
        os.startfile('data\\sound effects\\Vairo - SWARA(MP3_160K).mp3')
        sleep(2)
        click(x=500, y=800)
        print('installing required packages....\n')
        speak('installing required packages....')
        sleep(8)
        print('checking packages....')
        speak('checking packages')
        check2 = os.path.isdir('data')
        check3 = os.path.isdir('data\\admin')
        check4 = os.path.isdir('data\\sound effects')
        if check2 == True:
            print("FOLDER (data) SUCCESSFULLY INSTALLED")
            sleep(1.5)
        if check3 == True:
            print("FOLDER (admin) SUCCESSFULLY INSTALLED")
            sleep(1.5)
        if check4 == True:
            print("FOLDER (sound effects) SUCCESSFULLY INSTALLED\n")
            sleep(1.5)
        if check2 == False:
            print("FOLDER (data) NOT FOUND !")
            sleep(2)
            os.abort()
        if check3 == False:
            print("FOLDER (admin) NOT FOUND !")
            sleep(2)
            os.abort()
        if check4 == False:
            print("FOLDER (sound effects) NOT FOUND !")
            sleep(2)
            os.abort()
        speak('checking all modules')
        print('checking all modules....\n')
        sleep(10)
        speak('enter your admin name')
        admin_name = input('ENTER YOUR ADMIN NAME: ').lower()
        speak('enter your admin password')
        admin_password = input('ENTER YOUR ADMIN PASSWORD: ')
        speak('enter your phone number')
        phone_number = input('ENTER YOUR PHONE NUMBER: +91')
        speak('enter your e mail')
        email = input('ENTER YOUE E-MAIL: ')
        speak('enter your birth place')
        bp = input('ENTER YOUR birth place: ').lower()
        speak('enter your favourite colourl')
        fc = input('ENTER YOUR favourite colour: ').lower()
        os.system('cls')
        speak('RE-ENTER YOUR PASSWORD')
        repass = input("RE-ENTER YOUR PASSWORD: ")
        os.system('cls')
        if repass == admin_password:
            print('----------YOUR ENTERED INFORMATION---------')
            sleep(2)
            print('\n')
            print('YOUR NAME: ',admin_name)
            print('YOUR PHONE NUMBER: ',phone_number)
            print('YOUR E-MAIL: ',email)
            print('YOUR FAVOURITE COLOUR: ',fc)
            print('YOUR BIRTH PLACE: ',bp)
            print('\n')
            a = input('press "ENTER" to continue...')
            os.system('cls')
            up = '12345'
            do = '67890'
            c = up + do
            lenght = 4
            gen = "".join(random.sample(c,lenght))
            os.mkdir('data\\admin\\'+admin_name+gen)
            print('YOUR USERNAME IS: ',admin_name+gen)
            print('dont forget it !')
            asad = input('PRESS ENTER TO CONTINUE>>>')
            file = open('data\\admin\\'+admin_name+gen+'\\name.txt', 'w+')
            file.write(admin_name)
            file.close()
            file = open('data\\admin\\'+admin_name+gen+'\\phone_number.txt', 'w+')
            file.write(phone_number)
            file.close()
            file = open('data\\admin\\'+admin_name+gen+'\\email.txt', 'w+')
            file.write(email)
            file.close()
            def paEncrypt():
                key = Fernet.generate_key()
                file2 = open('data\\admin\\'+admin_name+gen+'\\key.key','wb')
                file2.write(key)
                file2.close()
                file3 = open('data\\admin\\'+admin_name+gen+'\\key.key','rb')
                key = file3.read()
                file3.close()
            
                with open('data\\admin\\'+admin_name+gen+'\\passcode.txt','rb') as f:
                    data = f.read()
            
                fernet = Fernet(key)
                encrypted = fernet.encrypt(data)
            
                with open('data\\admin\\'+admin_name+gen+'\\enPASS.txt.encrypt','wb') as f:
                    f.write(encrypted)
                os.remove('data\\admin\\'+admin_name+gen+'\\passcode.txt')
            file = open('data\\admin\\'+admin_name+gen+'\\passcode.txt','w')
            file.write(str(repass))
            file.close()
            paEncrypt()
            os.system('cls')
            print('\t\t\t\tâï¸ ğğğğğ âï¸\n\n')
    
            file = open('data\\admin\\'+admin_name+gen+'\\fc.txt','w')
            file.write(str(fc))
            file.close()
            key = Fernet.generate_key()
            file2 = open('data\\admin\\'+admin_name+gen+'\\2key.key','wb')
            file2.write(key)
            file2.close()
            file3 = open('data\\admin\\'+admin_name+gen+'\\2key.key','rb')
            key = file3.read()
            file3.close()
        
            with open('data\\admin\\'+admin_name+gen+'\\fc.txt','rb') as f:
                data = f.read()
                
            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)
        
            with open('data\\admin\\'+admin_name+gen+'\\enFC.txt.encrypt','wb') as f:
                f.write(encrypted)
            os.remove('data\\admin\\'+admin_name+gen+'\\fc.txt')
    
    
    
            file = open('data\\admin\\'+admin_name+gen+'\\bp.txt','w')
            file.write(str(bp))
            file.close()
            key = Fernet.generate_key()
            file2 = open('data\\admin\\'+admin_name+gen+'\\3key.key','wb')
            file2.write(key)
            file2.close()
            file3 = open('data\\admin\\'+admin_name+gen+'\\3key.key','rb')
            key = file3.read()
            file3.close()
        
            with open('data\\admin\\'+admin_name+gen+'\\bp.txt','rb') as f:
                data = f.read()
                
            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)
        
            with open('data\\admin\\'+admin_name+gen+'\\enBP.txt.encrypt','wb') as f:
                f.write(encrypted)
            os.remove('data\\admin\\'+admin_name+gen+'\\bp.txt')
            
            os.system('cls')
            print('\t\t\tâå½¡[ê±ÉªÉ¢É´ á´á´ á´¡á´ê± ê±á´á´á´á´ê±ê±ê°á´Ê]å½¡â\n\n')
        else:
            print('password does not match !')
            speak('password does not match')
            sleep(3)
            os.abort()


        os.mkdir('data\\admin\\successfull')
        sleep(2)
        os.system('cls')
        speak('restarting in...')
        print('restarting in...')
        print('3')
        speak('3')
        print('2')
        speak('2')
        print('1')
        speak('1')
        os.startfile('settings.exe')
        os.abort() 

# CALLS LOGIN FUNCTION
login_signup()