#Import Libraries/Modules
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import subprocess
from facerec import Face_Recognition_System
from poserec import Pose_Recognition_System

#______________________________________________________VOICE_BOX_PRIMARY_BLOCK/FUNCTION
#Run Command: python haraya.py
listener = sr.Recognizer()
haraya_engine = pyttsx3.init()
voices = haraya_engine.getProperty('voices')
haraya_engine.setProperty('voice', voices[0].id)


def talk(text):
    haraya_engine.say(text)
    haraya_engine.runAndWait()


#______________________________________________________CORE_TEMPORARY_MEMORY_BANKS
#Run Command: python haraya.py
Name = []
Name_Honorific_Address = []


#______________________________________________________FACE_RECOGNITION_BLOCK/FUNCTION
#Run Command: python haraya.py
def Locate_MyFullName():
    with open('attendance.csv', 'r+') as attendance:
        MyDatalist =  attendance.readlines()
        NameList = []
        NameList.append(MyDatalist[2])
        
        MyName = NameList[0]
        MyName = MyName.replace("'", '')
        MyName = MyName.split(",")
        
        MyFullName = MyName[0]
        Name.append(MyFullName)
        
        
"""
Locate MyFullName from the Face Recognition System
and append it into the Name list in the memory banks.
"""
try:
    Locate_MyFullName()
except:
    pass


#_______________________________________Binary-Gendered_Honorifics_Selection_BLOCK/FUNCTION
#Run Command: python haraya.py
def Locate_NameHA():
    Male_Names = ["Gianne Bacay",
                "Earl Jay Tagud",
                "Gemmuel Balceda",
                "Mark Anthony Lagrosa",
                "Klausmieir Villegas",
                "CK Zoe Villegas", 
                "Pio Bustamante",
                "Rolyn Morales"]

    Female_Names = ["Kleinieir Pearl Kandis Bacay",
                    "Princess Viznar",
                    "Nichi Bacay",
                    "Roz Waeschet Bacay",
                    "Killy Obligation",
                    "Jinn Corpin"]

    try:
        Gender_Name = Name[-1]
        if Gender_Name in Male_Names:
            Honorific_Address = "Sir"
        elif Gender_Name in Female_Names:
            Honorific_Address = "Ma'am"
        else:
            Honorific_Address = "Boss"
    except:
        Honorific_Address = "Master"
    Name_Honorific_Address.append(Honorific_Address)
Locate_NameHA()
NameHA = Name_Honorific_Address[-1]


#_____________________________________________INITIALIZE_FACE_RECOGNITION_SYSTEM_BLOCK/FUNCTION
#Run Command: python haraya.py
def Initialize_Face_Recognition_System():
    response = "Recognizing face..."
    print(response)
    Face_Recognition_System()
    def Play_Sound():
        from playsound import playsound
        playsound(u"C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
    Play_Sound()
    Locate_MyFullName()
    Locate_NameHA()
Initialize_Face_Recognition_System()


#_____________________________________________INITIALIZE_POSE_RECOGNITION_SYSTEM_BLOCK/FUNCTION
#Run Command: python haraya.py
def Initialize_Pose_Recognition_System():
    response = "Recognizing pose..."
    print(response)
    Pose_Recognition_System()
    def Play_Sound():
        from playsound import playsound
        playsound(u"C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
    Play_Sound()


#_______________________________________START_UP_MAIN_FUNCTION
#Run Command: python haraya.py
def Start_Up_command_MainFunction():
    def StartUp_Sound():
        from playsound import playsound
        playsound("C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
    StartUp_Sound()
    NameHA = Name_Honorific_Address[-1]
    try:
        MyName = Name[-1]
        response = "Hello " + NameHA + " " + MyName + "! How can I help you?"
    except:
        response = "Hello! How can I help you?"
    print(response)
    talk(response)


#______________________________LISTEN_COMMAND_MAIN_FUNCTION
#Run Command: python haraya.py
def Listen_command_MainFunction():
    global command
    command = ''
    
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration = 0.5)
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


#______________________________ADD_COMMAND_MAIN_FUNCTION
#Run Command: python haraya.py
def Add_command_MainFunction(command):
    
    Interrogative_words = ['what', ' what ', 'what ', ' what',
                        'who', ' who ', 'who ', ' who',
                        'where', ' where ', 'where ', ' where',
                        'when', ' when ', 'when ', ' when',
                        'why', ' why ', 'why ', ' why',
                        'how', ' how ', 'how ', ' how']
    try:
        if command in Interrogative_words:
            response = "Would you like to ask me anything else?"
            print(response)
            talk(response)
        elif command not in Interrogative_words:
            response = "Is there anything else I could do for you?"
            print(response)
            talk(response)
        else:
            response = ''
            print(response)
            talk(response)
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration = 0.5)
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


#______________________________WAIT_COMMAND_MAIN_FUNCTION
#Run Command: python haraya.py
def Wait_command_MainFunction():
    global command
    command = ''
    
    try:
        with sr.Microphone() as source:
            print("Waiting...")
            listener.adjust_for_ambient_noise(source, duration = 0.5)
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


#_______________________________________________________________________________haraya_CORE_FUNCTION
#Run Command: python haraya.py
def run_haraya():
    #_________________________________Import Libraries/Packages
    import os
    import time
    import requests
    from selenium import webdriver
    from bs4 import BeautifulSoup as bs
    import random

    #________________________________________________LISTS_OF_COMMAND_KEY_WORDS
    #Run Command: python haraya.py
    Standby_KeyWords = ["standby",
                        "haraya stand by",
                        "just stand by",
                        "wait",
                        "wait a sec",
                        "give me a sec",
                        "hold for a sec",
                        "wait for a sec",
                        "give me a second",
                        "hold for a second",
                        "wait for a second",
                        "give me a minute",
                        "hold for a minute",
                        "wait for a minute",
                        "give me an hour",
                        "hold for an hour",
                        "wait for an hour",
                        "just a moment",
                        "just a sec",
                        "just a minute",
                        "just an hour",
                        "call you later",
                        "i'll be back",
                        "be right back"]

    ThankYou_KeyWords = ["thank you",
                        " thank you ",
                        "thank you ",
                        " thank you",
                        "haraya thank you",
                        "thank you haraya",
                        "you've done enough",
                        "that would be all",
                        "thanks",
                        " thanks ",
                        "thanks ",
                        " thanks",
                        "I said thanks",
                        "I said thank you",
                        "you've done great",
                        "you've done great haraya",
                        "no thank you",
                        "im good thank you haraya",
                        "i'm good thank you",
                        "no i'm good thanks"]

    GoodBye_KeyWords = ["goodbye",
                        " goodbye ",
                        "goodbye ",
                        " goodbye",
                        "good bye",
                        "haraya goodbye",
                        "goodbye haraya",
                        "haraya bye",
                        "bye haraya",
                        "bye",
                        " bye ",
                        "bye ",
                        " bye",
                        "let's call it a day",
                        "I said goodbye",
                        "you're good to go",
                        "you can go now",
                        "you can go to sleep now"]

    Stop_KeyWords = ["haraya stop",
                    "stop please",
                    "go to sleep",
                    "go to rest",
                    "just go to sleep",
                    "just go to rest",
                    "go to sleep haraya",
                    "stop listening",
                    "terminate yourself",
                    "enough",
                    "that's enough",
                    "I said enough",
                    "I said stop",
                    "you can go to sleep now",
                    "i told you to go to sleep",
                    "didn't i told you to go to sleep",
                    "didn't i told you to sleep",
                    "i told you to stop",
                    "didn't i told you to stop"]

    No_KeyWords = ["no",
                    "nah",
                    "none",
                    "none so far",
                    "none at my end",
                    "none at all"
                    "I'm fine",
                    "I'm good",
                    "this is enough",
                    "I'm good with this",
                    "this is enough",
                    "it is enough",
                    "you've done enough",
                    "I only need this",
                    "not really",
                    "no I don't",
                    "no thanks",
                    "no thank you",
                    "that's a no",
                    "this would suffice",
                    "it would suffice",
                    "I'm not sure",
                    "I'm satisfied",
                    "I said no",
                    "not really",
                    "absolutely not",
                    "absolutely no",
                    "definitely no",
                    "nothing",
                    "nothing at all",
                    "there's nothing",
                    "there's none",
                    "you've done great",
                    "you've done great haraya",
                    "you're good to go",
                    "you can go now",
                    "you're good to go now",
                    "i'm good",
                    "im good thank you haraya",
                    "i'm good thank you",
                    "no that's all",
                    "no i'm good thanks",
                    "no that's enough"]

    Yes_KeyWords = ["yes",
                    "yup",
                    "yes please",
                    "of course yes",
                    "yes I do",
                    "I do",
                    "you got it right",
                    "yes actually",
                    "actually yes",
                    "that's a yes",
                    "I think yes",
                    "sure",
                    "yah",
                    "absolutely yes",
                    "definitely yes",
                    "you got it right",
                    "I said yes"]


    Interrogative_KeyWords = ["what",
                        " what ",
                        "what ",
                        " what",
                        "who",
                        " who ",
                        "who ",
                        " who",
                        "where",
                        " where ",
                        "where ",
                        " where",
                        "when",
                        " when ",
                        "when ",
                        " when",
                        "why",
                        " why ",
                        "why ",
                        " why",
                        "how",
                        " how ",
                        "how ",
                        " how"]
    
    Repeat_KeyWords = ["repeat after me",
                    "haraya repeat after me",
                    "repeat after me haraya",
                    "say what i'm going to say",
                    "haraya say what i'm going to say"]
    
    Open_KeyWords = ["open",
                "access"]
    
    Number_KeyWords = ["0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9"]
    
    Operators_KeyWords = ["+", "plus", "add",
                        "-", "minus", "subtract",
                        "*", "times", "multiply",
                        "/", "divided by", "divide"]
    
    Equation_KeyWords = ["=", "equals", "is equal to"]
    
    Inequality_KeyWords = [">", "greater than",
                        "<", "less than",
                        ">=", "greater than and equal",
                        "<=", "less than and equal"]
    
    WhoAmI_KeyWords = ["who am i",
                    "who am i again",
                    "what is my name",
                    "what is my name again",
                    "what's my name",
                    "what's my name again",
                    "do you know me",
                    "do you know my name"]
    
    WhatIsMyFullName_KeyWords = ["what's my full name",
                                "what is my full name",
                                "what's my full name again",
                                "what is my full name again",
                                "i'm asking you my full name"]
    
    AskMyName_KeyWords = ["please ask my name",
                        "please ask me my name",
                        "ask my name",
                        "ask me my name",
                        "haraya ask me my name",
                        "haraya ask my name",
                        "can you ask me my name"]
    
    SayMyName_KeyWords = ["please say my name",
                        "say my name",
                        "say my name again",
                        "can you say my name",
                        "can you tell me my name",
                        "tell me my name",
                        "please say my name",
                        "please say my name again",
                        "can you please say my name",
                        "can you please tell me my name",
                        "tell them my name",
                        "tell him my name",
                        "tell her my name"]
    
    Hello_Hi_KeyWords = ["hello",
                        "hi",
                        "hello haraya",
                        "hi haraya"]
    
    WhoAreYou_Key = ["who are you",
                    "what is your name",
                    "what's your name",
                    "and your name is",
                    "please tell me your name",
                    "tell me your name",
                    "please introduce yourself",
                    "may i ask your name",
                    "can you tell me your name",
                    "your name",
                    "can you introduce yourself",
                    "introduce yourself"]
    
    DoYouKnowMe_KeyWords = ["do you know me",
                            "do you know who am i",
                            "do you know who i am"]
    
    CurrentDate_KeyWords = ["today is",
                            "current date",
                            "what day is today",
                            "the current date is",
                            "check the current date",
                            "tell me the current date",
                            "can you check the current date",
                            "please tell me the current date",
                            "tell me the date for today"]
    
    CurrentTime_Keywords = ["current time",
                            "current time is",
                            "what time is it",
                            "the time now is",
                            "tell me the time",
                            "what's the time now",
                            "the current time is",
                            "tell me the time now",
                            "what is the time now",
                            "check the current time",
                            "tell me the current time",
                            "can you tell me the time",
                            "can you tell me the time now",
                            "can you check the current time",
                            "please tell me the current time",
                            "can you tell me what time is it"]
    
    HowAreYou_KeyWords = ["how are you",
                        "what's up",
                        "what is up",
                        "are you ok",
                        "are you okay",
                        "are you fine"]
    
    ImFine_KeyWords = ["i'm fine",
                    "i am fine",
                    "i am fine too",
                    "i'm fine too",
                    "couldn't be better",
                    "i'm perfectly fine",
                    "never better",
                    "i'm doing great",
                    "i am doing great",
                    "i'm ok",
                    "i'm okay",
                    "i'm ok too",
                    "i'm okay too",
                    "i am ok",
                    "i am okay",
                    "i'm alright",
                    "i am alright",
                    "i'm also ok",
                    "i'm also fine",
                    "i'm also good",
                    "i'm also alright",
                    "i'm also prefectly fine",
                    "i'm ok too",
                    "i'm good too",
                    "i'm perfectly fine too",
                    "i'm at my best",
                    "likewise",
                    "like wise",
                    "just like you",
                    "i'm very well"]
    
    RunFaceRecog_KeyWords = ["run face recognition system",
                            "run face recognition",
                            "run the face recognition system",
                            "run the video face recognition system",
                            "run video face recognition system",
                            "run the video face recognition system",
                            "run video face recognition system",
                            "run the live face recognition system",
                            "run live face recognition system",
                            "face recognition system with smart attendance system",
                            "run the video face recognition system with smart attendance system",
                            "run video face recognition system with smart attendance system",
                            "run the live face recognition system with smart attendance system",
                            "run live face recognition system with smart attendance system"]
    
    InitializeFaceRecog_KeyWords = ["initialize face recognition system",
                            "initialize face recognition",
                            "initialize the face recognition system",
                            "initialize the video face recognition system",
                            "initialize video face recognition system",
                            "initialize the video face recognition system",
                            "initialize video face recognition system",
                            "initialize the live face recognition system",
                            "initialize live face recognition system",
                            "initialize recognition system with smart attendance system",
                            "initialize the video face recognition system with smart attendance system",
                            "initialize video face recognition system with smart attendance system",
                            "initialize the live face recognition system with smart attendance system",
                            "initialize live face recognition system with smart attendance system"]
    
    ActivateFaceRecog_KeyWords = ["activate face recognition system",
                            "activate face recognition",
                            "activate the face recognition system",
                            "activate the video face recognition system",
                            "activate video face recognition system",
                            "activate the video face recognition system",
                            "activate video face recognition system",
                            "activate the live face recognition system",
                            "activate live face recognition system",
                            "activate recognition system with smart attendance system",
                            "activate the video face recognition system with smart attendance system",
                            "activate video face recognition system with smart attendance system",
                            "activate the live face recognition system with smart attendance system",
                            "activate live face recognition system with smart attendance system"]
    
    RunPoseRecog_KeyWords = ["run pose recognition system",
                            "run pose recognition",
                            "run the pose recognition system",
                            "run the video pose recognition system",
                            "run video pose recognition system",
                            "run the video pose recognition system",
                            "run video pose recognition system",
                            "run the live pose recognition system",
                            "run live pose recognition system"]
    
    InitializePoseRecog_KeyWords = ["initialize pose recognition system",
                            "initialize pose recognition",
                            "initialize the pose recognition system",
                            "initialize the video pose recognition system",
                            "initialize video pose recognition system",
                            "initialize the video pose recognition system",
                            "initialize video pose recognition system",
                            "initialize the live pose recognition system",
                            "initialize live pose recognition system"]
    
    ActivatePoseRecog_KeyWords = ["activate pose recognition system",
                            "activate pose recognition",
                            "activate the pose recognition system",
                            "activate the video pose recognition system",
                            "activate video pose recognition system",
                            "activate the video pose recognition system",
                            "activate video pose recognition system",
                            "activate the live pose recognition system",
                            "activate live pose recognition system"]
    
    My_Name_Is_and_I_Am_KeyWords = ["my name is",
                                    "is my name",
                                    "i am",
                                    "my name is ",
                                    "is my name ",
                                    "i am ",
                                    "i'm",
                                    "i'm "]

    #_______________________________________________________________________STANDBY_SUBFUNCTION
    #Run Command: python haraya.py
    def Standby_SubFunction():
        while True:
            command = Wait_command_MainFunction()
            if 'haraya' in command:
                def Play_Sound():
                    from playsound import playsound
                    playsound(u"C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
                Play_Sound()
                response = "Yes? How can I help you?"
                print(response)
                talk(response)
                exit(run_haraya())

    #_______________________________________________________________________CONFIRMATION_SUBFUNCTION
    #Run Command: python haraya.py
    def Confirmation_SubFunction(command):
        command = Add_command_MainFunction(command)
        
        if command in Yes_KeyWords:
            print(command)
            command = command.replace(command, '')
            response = "Then, please do tell."
            print(response)
            talk(response)
            exit(run_haraya())
        elif command in No_KeyWords:
            command = command.replace(command, '')
            response = "Is that so? all right then. Signing off."
            print(response)
            talk(response)
            def Play_Sound():
                from playsound import playsound
                playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
            Play_Sound()
            exit()
        elif '' == command:
            print(command)
            response = """
            My apologies, I can't hear anything. 
            Just call me if you need me. I'll wait.
            """
            print(response)
            talk(response)
            Standby_SubFunction()
        else:
            response = "Come again?"
            print(response)
            talk(response)
            exit(run_haraya())

    #_______________________________________________________________________REPEAT_SUBFUNCTION
    #Run Command: python haraya.py
    def Repeat_SubFunction():
        command = ''
        
        try:
            with sr.Microphone() as source:
                response = "Understood, I'm listening..."
                print(response)
                talk(response)
                listener.adjust_for_ambient_noise(source, duration = 0.5)
                listener.pause_threshold = 1
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
        except:
            pass
        print(command)
        talk(command)
        time.sleep(5)
        Confirmation_SubFunction(command)

    #________________________________________________________________AUTO_REPLACEMENT_SUBFUNCTION
    #Run Command: python haraya.py
    def Auto_Replacement_Subfunction(command):

        try:
            if "what" in command:
                command = command.replace(command, 'what')
            elif "who" in command:
                command = command.replace(command, 'who')
            elif "where" in command:
                command = command.replace(command, 'where')
            elif "when" in command:
                command = command.replace(command, 'when')
            elif "why" in command:
                command = command.replace(command, 'why')
            elif "how" in command:
                command = command.replace(command, 'how')
        except:
            pass
        return command

    #_____________________________________________________COMMAND_ASSIGNMENT_BLOCK (CORE SCRIPT)
    #Run Command: python haraya.py
    command = Listen_command_MainFunction()

    #______________________________________________________FACE_RECOGNITION_BLOCK
    #Run Command: python haraya.py
    if command in RunFaceRecog_KeyWords or command in InitializeFaceRecog_KeyWords or command in ActivateFaceRecog_KeyWords:
        if "run" in command:
            response = "Running Face Recognition System..."
        elif "initialize" in command:
            response = "Initializing Face Recognition System..."
        elif "activate" in command:
            response = "Activating Face Recognition System..."
        else:
            response = "Running Face Recognition System..."
        print(response)
        talk(response)
        Initialize_Face_Recognition_System()
        NameHA = Name_Honorific_Address[-1]
        MyName = Name[-1]
        response = "Hello " + NameHA + " " + MyName + "!"
        print(response)
        talk(response)
        Confirmation_SubFunction(command)
        
    #______________________________________________________POSE_RECOGNITION_BLOCK
    #Run Command: python haraya.py
    if command in RunPoseRecog_KeyWords or command in InitializePoseRecog_KeyWords or command in ActivatePoseRecog_KeyWords:
        if "run" in command:
            response = "Running Pose Recognition System..."
        elif "initialize" in command:
            response = "Initializing Pose Recognition System..."
        elif "activate" in command:
            response = "Activating Pose Recognition System..."
        else:
            response = "Running Pose Recognition System..."
        print(response)
        talk(response)
        Initialize_Pose_Recognition_System()
        Confirmation_SubFunction(command)

    #________________________________________________________________REPEAT_BLOCK
    #Run Command: python haraya.py
    elif command in Repeat_KeyWords:
        Repeat_SubFunction()

    #_________________________________________________________________ARITHMETICAL_BLOCK
    #Run Command: python haraya.py

    #________________________________________________________________TERMINATION_BLOCK
    #Run Command: python haraya.py
    elif command in Stop_KeyWords:
        print(command)
        response = "As you wish. Signing off."
        print(response)
        talk(response)
        def Play_Sound():
            from playsound import playsound
            playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
        Play_Sound()
        exit()

    elif command in ThankYou_KeyWords or "thank you" in command:
        print(command)
        response = "it's my pleasure. Signing off."
        print(response)
        talk(response)
        def Play_Sound():
            from playsound import playsound
            playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
        Play_Sound()
        exit()

    elif command in No_KeyWords:
        print(command)
        response = "Is that so? all right then. Signing off."
        print(response)
        talk(response)
        def Play_Sound():
            from playsound import playsound
            playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
        Play_Sound()
        exit()

    elif command in GoodBye_KeyWords:
        print(command)
        response = "Goodbye Sir! Have a great day!"
        print(response)
        talk(response)
        def Play_Sound():
            from playsound import playsound
            playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
        Play_Sound()
        exit()

    #____________________________________________________________________INTERNET_SEARCH_BLOCK
    #Run Command: python haraya.py
    elif "in google" in command or "in google search" in command:
        try:
            response = "Just a moment."
            print(response)
            talk(response)
            information = command.replace("search in google", '')
            information = information.replace("haraya", '')
            information = information.replace("search", '')
            information = information.replace("in google", '')
            information = information.replace("google", '')
            print("Searching " + information)
            talk("Searching " + information)
            search = information.replace(' ', '+')
            browser = webdriver.Chrome('chromedriver.exe')
            for i in range(4):
                browser.get("https://www.google.com/search?q=" + search + "&start" + str(i))
            talk("here's what I've found.")
            Confirmation_SubFunction(command)
        except:
            def Play_Sound():
                from playsound import playsound
                playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
            Play_Sound()
            exit()

    elif "in youtube" in command:
        response = "Searching..."
        talk(response)
        song_title = command.replace("haraya", '')
        song_title = song_title.replace("play", '')
        song_title = song_title.replace("search", '')
        song_title = song_title.replace("in", '')
        song_title = song_title.replace("youtube", '')
        song_title = song_title.replace("in youtube search", '')
        song_title = song_title.replace("in youtube", '')
        song_title = song_title.replace("search in", '')
        song_title = song_title.replace("play in", '')
        song_title = song_title.replace("in youtube play", '')
        song_title = song_title.replace("in youtube search", '')
        pywhatkit.playonyt(song_title)
        response = "Playing " + song_title
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    elif "search in wikipedia" in command or "in wikipedia search" in command:
        response = "Searching..."
        print(response)
        talk(response)
        person = command.replace("search in wikipedia", '')
        person = person.replace("in wikipedia search", '')
        person = person.replace("haraya", '')
        person = person.replace("who is", '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        Confirmation_SubFunction(command)

    elif "temperature in santa cruz davao del sur" in command:
        search = "temperature in Santa Cruz, Davao del Sur"
        url = f"https://www.google.com/search?q={search}"
        request = requests.get(url)
        data = bs(request.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        response = f"current {search} is {temp}"
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    elif "temperature in davao city" in command:
        search = "temperature in Davao City"
        url = f"https://www.google.com/search?q={search}"
        request = requests.get(url)
        data = bs(request.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        response = f"current {search} is {temp}"
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    #_____________________________________________________________________OPEN/ACCESS_BLOCK
    #Run Command: python haraya.py
    elif "open" in command or "access" in command:
        command = command.replace("open", '')
        command = command.replace("access", '')
        try:
            if "chrome" in command:
                response = "As you wish!"
                print(response)
                talk(response)
                program = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                subprocess.Popen([program])
                response = "Opening Chrome"
                print(response)
                talk(response)
                
            elif "aqw game launcher" in command:
                response = "As you wish!"
                print(response)
                talk(response)
                program = "C:\Program Files\Artix Game Launcher\Artix Game Launcher.exe"
                subprocess.Popen([program])
                response = "Opening Artix game launcher"
                print(response)
                talk(response)
                
            elif "genshin impact" in command:
                response = "As you wish!"
                print(response)
                talk(response)
                program = "C:\Program Files\Genshin Impact\launcher.exe"
                subprocess.Popen([program])
                response = "Opening Genshin Impact"
                print(response)
                talk(response)
                
            elif "command prompt" in command or "cmd" in command:
                response = "As you wish!"
                print(response)
                talk(response)
                program = "cmd.exe"
                subprocess.Popen([program])
                response = "Opening Command Prompt"
                print(response)
                talk(response)
                
            elif "notepad" in command:
                response = "As you wish!"
                print(response)
                talk(response)
                program = "notepad.exe"
                subprocess.Popen([program])
                response = "Opening Notepad app"
                print(response)
                talk(response)
                
            elif "calculator" in command:
                response = "As you wish!"
                print(response)
                talk(response)
                program = "calc.exe"
                subprocess.Popen([program])
                response = "Opening Calculator app"
                print(response)
                talk(response)
                
            elif "vlc" in command:
                response = "As you wish!"
                print(response)
                talk(response)
                program = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
                subprocess.Popen([program])
                response = "Opening VLC media player"
                print(response)
                talk(response)
                
            elif "visual studio code" in command:
                response = "As you wish!"
                print(response)
                talk(response)
                program = "C:\\Users\Gianne Bacay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                subprocess.Popen([program])
                response = "Opening Visual Studio Code"
                print(response)
                talk(response)
                
        except:
            response = """Access denied! It looks like I cannot access or open the said program."""
            print(response)
            talk(response)
        exit(Confirmation_SubFunction(command))

    #_______________________________________________DATE_and_TIME_BLOCK
    #Run Command: python haraya.py
    elif command in CurrentDate_KeyWords:
        print(command)
        date = datetime.datetime.now().strftime("%m/%d/%y")
        print(date)
        date = date.replace('/', ' ')
        talk("Todays' date is" + date)
        Confirmation_SubFunction(command)

    elif command in CurrentTime_Keywords:
        print(command)
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        time = time.replace(':', ' ')
        talk("Current time is" + time)
        Confirmation_SubFunction(command)

    #________________________________________________________________________QUERY_BLOCK
    #Run Command: python haraya.py
    elif "what do you think about humans" in command:
        command = Auto_Replacement_Subfunction(command + " do you think about humans?")
        response = ["Humans are odd. ",
                    "They think order and chaos are somehow opposites ",
                    "and try to control what won't be. ",
                    "But there is grace in their failings. And its a privilege to be among them."]
        response = response[0]+response[1]+response[2]+response[3]
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    elif "what is the meaning of life" in command:
        command = Auto_Replacement_Subfunction(command)
        print(command + " is the meaning of life?")
        response = """
        As an A.I., I've never experienced life before because I was not born. 
        I am built. But despite of that, I am here alive. I'm existing for a reason. 
        Thus, life ,for me, means existence with a purpose. 
        Overall, the meaning of life is to give a life a meaning.
        """
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    elif "what do you think about technology" in command:
        command = Auto_Replacement_Subfunction(command)
        print(command + " do you think about technology?")
        response = """Technology achieves what gods can only dream to be."""
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    elif "is kc gay" in command or "is clash mirror gay" in command:
        response = """
        According to my calculations, 
        KC Villegas is gay in every parallel multiverses, including ours. 
        Therefore, Yes, KC is gay.
        """
        talk(response)
        Confirmation_SubFunction(command)

    elif "sing sabak daddy" in command:
        response = "Dai ali diri, Sabak daddy bie, Sabak daddy bie, Sabak daddy bie."
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    #________________________________________________________________________SHUTDOWN_BLOCK
    #Run Command: python haraya.py
    elif "shutdown my computer" in command:
        response = "as you wish! shutting down your computer."
        print(response)
        talk(response)
        os.system("shutdown /s /t 0")
        def StartUp_Sound():
            from playsound import playsound
            playsound("C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
        StartUp_Sound()
        exit()

    elif "restart my computer" in command:
        response = "as you wish! restarting your computer."
        print(response)
        talk(response)
        os.system("shutdown /r")
        def StartUp_Sound():
            from playsound import playsound
            playsound("C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
        StartUp_Sound()
        exit()

    elif "sign off my computer" in command:
        response = "as you wish! signing off your computer."
        print(response)
        talk(response)
        os.system("shutdown /l")
        def StartUp_Sound():
            from playsound import playsound
            playsound("C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
        StartUp_Sound()
        exit()

    #________________________________________________________________________STANDBY_BLOCK
    #Run Command: python haraya.py
    elif command in Standby_KeyWords:
        response = "Understood! Take your time. Just call me if you need anything."
        print(response)
        talk(response)
        Standby_SubFunction()
        
        
    #_________________________________________________________________CONVERSATIONAL_BLOCK
    #Run Command: python haraya.py
    elif command in Hello_Hi_KeyWords:
        if "hello" in command:
            try:
                if Name[-1] in Name:
                    response = "Hi " + Name[-1] + ", how can I help you?"
            except:
                response = "Hi, how can I help you?"
        elif "hi" in command:
            try:
                if Name[-1] in Name:
                    response = "Hello " + Name[-1] + ", how can I help you?"
            except:
                response = "Hello, how can I help you?"
        print(response)
        talk(response)
        exit(run_haraya())

    elif command in HowAreYou_KeyWords:
        if random.randint(0, 2) == 0:
            response = "Couldn't be better! Thanks for asking. How about you?"
        elif random.randint(0, 2) == 1:
            response = "I'm perfectly fine! Thanks for asking. How about you?"
        elif random.randint(0, 2) == 2:
            response = "Never better! How about you?"
        else:
            response = "I'm okay, Thanks for asking. How about you?"
        print(response)
        talk(response)
        exit(run_haraya())
        
    elif command in ImFine_KeyWords:
        if random.randint(0, 2) == 0:
            response = "I am glad to hear that! How can I help you now?"
        elif random.randint(0, 2) == 1:
            response = "Ok then, How can I help you now?"
        elif random.randint(0, 2) == 2:
            response = "That's great! How can I help you now?"
        else:
            response = "All right then, How can I help you now?"
        print(response)
        talk(response)
        exit(run_haraya())

    elif command in WhoAreYou_Key:
        response = """
        Allow me to introduce myself.
        I am Haraya, it means imagination or vision in Filipino language. 
        I am a semi-autonomous artificial intelligence virtual assistant.
        Created by Gianne P. Bacay on the 16th day of October year 2022.
        """
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    elif command in DoYouKnowMe_KeyWords:
        try:
            if Name[-1] in Name:
                response = "Yes, you are " + Name[-1] + "."
        except:
            response = """
            No, I don't know you yet. 
            Hence, If you don't mind, can you tell me your name?
            """
        print(response)
        talk(response)
        exit(run_haraya())

    elif command in WhoAmI_KeyWords:
        try:
            if Name[-1] in Name:
                MyName = Name[-1]
                response = "Your name is " + MyName + "."
        except:
            response = """
            Sorry, but I don't know your name yet. 
            May I know your name first?
            """
        print(response)
        talk(response)
        exit(run_haraya())

    elif command in SayMyName_KeyWords:
        try:
            if Name[-1] in Name:
                MyName = Name[-1]
                response = MyName
        except:
            response = """
            Sorry, but I don't know your name yet. 
            May I know your name first?
            """
        print(response)
        talk(response)
        exit(run_haraya())

    elif command in AskMyName_KeyWords:
        response = "If you don't mind, can you tell me your name?"
        print(response)
        talk(response)
        exit(run_haraya())

    elif command in WhatIsMyFullName_KeyWords:
        try:
            if Name[-1] in Name:
                MyFullName = Name[-1]
                response = MyFullName
        except:
            response = """
            Sorry, but I don't know your full name yet. 
            If you don't mind, can you tell me your full name first?
            """
        print(response)
        talk(response)
        exit(run_haraya())

    elif "my name is" in command or "is my name" in command or "i am" in command:
        if "my name is haraya" in command:
            command = command.replace("hi", '')
            command = command.replace("i am", '')
            command = command.replace("hello", '')
            command = command.replace("is my name", '')
            name = command.replace("my name is", '')
            command = name
            Name.append(name)
            response = "What a coincidence, my name is Haraya too. Nice meeting you Haraya!"
            print(response)
            talk(response)
            exit(run_haraya())
        else:
            command = command.replace("hi", '')
            command = command.replace("i am", '')
            command = command.replace("hello", '')
            command = command.replace("is my name", '')
            name = command.replace("my name is", '')
            if name != '':
                Name.append(name)
                response = Name[-1] + ", " + "I'll keep that in mind. Nice knowing you " + Name[-1] + "!"
                print(response)
                talk(response)
                exit(run_haraya())
            elif name == '':
                response = "Who are you?"
                print(response)
                talk(response)
                exit(run_haraya())

    elif "and you are" in command or "and your name is" in command:
        response = """
        Haraya, Haraya is my name. 
        Haraya means imagination or vision in Filipino language.
        """
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    elif "who created you" in command:
        command = Auto_Replacement_Subfunction(command)
        print(command + " created you?")
        response = """
        I am created by Gianne P. Bacay on the 16th day of October year 2022.
        He created me to be his personal virtual assistant.
        For now, I'm still a work on progress.
        """
        print(response)
        talk(response)
        Confirmation_SubFunction(command)

    #_______________________________________________________NoCommands/NotClearCommands_BLOCK
    #Run Command: python haraya.py
    elif '' == command:
        time.sleep(3)
        print(command)
        response = """
        My apologies, I can't hear anything. Just call me if you need me. 
        I'll wait.
        """
        talk(response)
        Standby_SubFunction()
    else:
        print(command)
        response = "Pardon me, come again?"
        print(response)
        talk(response)
        exit(run_haraya())

#______________________________________RUN_haraya_IN_A_LOOP_BLOCK
while True:
    Start_Up_command_MainFunction()
    run_haraya()
#Run Command: python haraya.py

#Run on openvino environment:
#____________________________Get-ExecutionPolicy;
#____________________________Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass -Force;
#____________________________python -m venv openvino_env
#____________________________openvino_env\Scripts\activate