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
#Run Command: python jarvis.py
listener = sr.Recognizer()
jarvis_engine = pyttsx3.init()
voices = jarvis_engine.getProperty('voices')
jarvis_engine.setProperty('voice', voices[0].id)


def speak(text):
    jarvis_engine.say(text)
    jarvis_engine.runAndWait()


#______________________________________________________CORE_TEMPORARY_MEMORY_BANKS
#Run Command: python jarvis.py
Name = []
Name_Honorific_Address = []
Arithmetic_Addition = []
Arithmetic_Subtraction = []
Arithmetic_Multiplication = []
Arithmetic_Division = []
Arithmetic_Modulo = []
Date = []

#______________________________________________________FACE_RECOGNITION_BLOCK/FUNCTION
#Run Command: python jarvis.py
def Locate_MyFullName():
    with open("C:\\Users\\Gianne Bacay\\Desktop\\VIRTUAL_ASSISTANT_SYSTEM\\VIRTUAL-ASSISTANT-AI-PROJECT\\Virtual_Assistant_AI_Project\\attendance.csv", "r+") as attendance:
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
#Run Command: python jarvis.py
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
#Run Command: python jarvis.py
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
#Run Command: python jarvis.py
def Initialize_Pose_Recognition_System():
    response = "Recognizing pose..."
    print(response)
    Pose_Recognition_System()
    def Play_Sound():
        from playsound import playsound
        playsound(u"C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
    Play_Sound()


#_______________________________________START_UP_MAIN_FUNCTION
#Run Command: python jarvis.py
def Start_Up_command_MainFunction():
    def StartUp_Sound():
        from playsound import playsound
        playsound("C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
    StartUp_Sound()
    NameHA = Name_Honorific_Address[-1]
    try:
        MyName = Name[-1]
        response = "Hi " + NameHA + " " + MyName + "! How can I help you?"
    except:
        response = "Hi! How can I help you?"
    print(response)
    speak(response)


#______________________________LISTEN_COMMAND_MAIN_FUNCTION
#Run Command: python jarvis.py
def Listen_command_MainFunction():
    global command
    command = ''
    
    try:
        with sr.Microphone() as source:
            print("Listening...")
            def Play_Sound():
                from playsound import playsound
                playsound(u"C:\\Users\\Gianne Bacay\\Desktop\\Listening.mp3")
            Play_Sound()
            listener.adjust_for_ambient_noise(source, duration = 0.5)
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


#______________________________ADD_COMMAND_MAIN_FUNCTION
#Run Command: python jarvis.py
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
            speak(response)
        elif command not in Interrogative_words:
            response = "Is there anything else I could do for you?"
            print(response)
            speak(response)
        else:
            response = ''
            print(response)
            speak(response)
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
#Run Command: python jarvis.py
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


#_______________________________________________________________________________jarvis_CORE_FUNCTION
#Run Command: python jarvis.py
def run_jarvis():
    #_________________________________Import Libraries/Packages
    import os
    import time
    import calendar
    import requests
    from selenium import webdriver
    from bs4 import BeautifulSoup as bs
    import random
    import re
    import pyautogui

    #________________________________________________LISTS_OF_COMMAND_KEY_WORDS
    #Run Command: python jarvis.py
    Standby_KeyWords = ["standby",
                        "jarvis stand by",
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
                        "jarvis thank you",
                        "thank you jarvis",
                        "you've done enough",
                        "that would be all",
                        "thanks",
                        " thanks ",
                        "thanks ",
                        " thanks",
                        "I said thanks",
                        "I said thank you",
                        "you've done great",
                        "you've done great jarvis",
                        "no thank you",
                        "im good thank you jarvis",
                        "i'm good thank you",
                        "no i'm good thanks"]

    GoodBye_KeyWords = ["goodbye",
                        " goodbye ",
                        "goodbye ",
                        " goodbye",
                        "good bye",
                        "jarvis goodbye",
                        "goodbye jarvis",
                        "jarvis bye",
                        "bye jarvis",
                        "bye",
                        " bye ",
                        "bye ",
                        " bye",
                        "let's call it a day",
                        "I said goodbye",
                        "you're good to go",
                        "you can go now",
                        "you can go to sleep now"]

    Stop_KeyWords = ["jarvis stop",
                    "stop please",
                    "go to sleep",
                    "go to rest",
                    "just go to sleep",
                    "just go to rest",
                    "go to sleep jarvis",
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
                    "you've done great jarvis",
                    "you're good to go",
                    "you can go now",
                    "you're good to go now",
                    "i'm good",
                    "im good thank you jarvis",
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
                    "jarvis repeat after me",
                    "repeat after me jarvis",
                    "say what i'm going to say",
                    "jarvis say what i'm going to say"]
    
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
                        "jarvis ask me my name",
                        "jarvis ask my name",
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
                        "hello jarvis",
                        "hi jarvis"]
    
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
                            "date check",
                            "current date",
                            "what day is today",
                            "the current date is",
                            "check the current date",
                            "tell me the current date",
                            "can you check the current date",
                            "please tell me the current date",
                            "tell me the date for today",
                            "tell me the date today",
                            "what is the date today"]
    
    CurrentTime_Keywords = ["time check",
                            "current time",
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
                        "are you fine",
                        "how are you jarvis",
                        "what's up jarvis",
                        "what is up jarvis",
                        "are you ok jarvis",
                        "are you okay jarvis",
                        "are you fine jarvis"]
    
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
                            "run face rec again",
                            "recognize my face again",
                            "face recognition again",
                            "run face recognition system",
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
    
    Roll_A_Die_KeyWords = ["roll a die",
                "roll a dice",
                "roll the die",
                "roll the dice",
                "jarvis roll a die",
                "jarvis roll a dice",
                "jarvis roll the die",
                "jarvis roll the dice",
                "roll a die jarvis",
                "roll a dice jarvis",
                "roll the die jarvis",
                "roll the dice jarvis",
                "roll again",
                "roll again jarvis",
                "jarvis roll again"]
    
    Coundown_KeyWords = ["countdown",
                        "set countdown",
                        "set the countdown to",
                        "start countdown",
                        "start the countdown",
                        "countdown again",
                        "do a count down"]

    #_______________________________________________________________________STANDBY_SUBFUNCTION
    #Run Command: python jarvis.py
    def Standby_SubFunction():
        while True:
            command = Wait_command_MainFunction()
            if 'jarvis' in command:
                def Play_Sound():
                    from playsound import playsound
                    playsound(u"C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
                Play_Sound()
                response = "Yes? How can I help you?"
                print(response)
                speak(response)
                exit(run_jarvis())

    #_______________________________________________________________________CONFIRMATION_SUBFUNCTION
    #Run Command: python jarvis.py
    def Confirmation_SubFunction(command):
        command = Add_command_MainFunction(command)
        
        if command in Yes_KeyWords:
            print(command)
            command = command.replace(command, '')
            response = "Then, please do tell."
            print(response)
            speak(response)
            exit(run_jarvis())
        elif command in No_KeyWords:
            command = command.replace(command, '')
            response = "Is that so? all right then. Signing off."
            print(response)
            speak(response)
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
            speak(response)
            Standby_SubFunction()
        else:
            response = "Come again?"
            print(response)
            speak(response)
            exit(run_jarvis())

    #_______________________________________________________________________REPEAT_SUBFUNCTION
    #Run Command: python jarvis.py
    def Repeat_SubFunction():
        command = ''
        
        try:
            with sr.Microphone() as source:
                response = "Understood, I'm listening..."
                print(response)
                speak(response)
                listener.adjust_for_ambient_noise(source, duration = 0.5)
                listener.pause_threshold = 1
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
        except:
            pass
        print(command)
        speak(command)
        time.sleep(5)
        Confirmation_SubFunction(command)

    #________________________________________________________________AUTO_REPLACEMENT_SUBFUNCTION
    #Run Command: python jarvis.py
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
    
    #______________________________________________________________________SPELLED_NUMBER_CONVERTER_SUBFUNCTION
    #Run Command: python jarvis.py
    def SpelledNumber_Converter(StrNumbers):
            # Create a dictionary with the spelled numbers as keys and their integer values as values
            number_words = {"zero": 0,
                            "one": 1,
                            "two": 2,
                            "three": 3,
                            "four": 4,
                            "five": 5,
                            "six": 6,
                            "seven": 7,
                            "eight": 8,
                            "nine": 9,
                            "ten": 10,
                            "eleven": 11,
                            "twelve": 12,
                            "thirteen": 13,
                            "fourteen": 14,
                            "fifteen": 15,
                            "sixteen": 16,
                            "seventeen": 17,
                            "eighteen": 18,
                            "nineteen": 19,
                            "twenty": 20,
                            "thirty": 30,
                            "forty": 40,
                            "fifty": 50,
                            "sixty": 60,
                            "seventy": 70,
                            "eighty": 80,
                            "ninety": 90,
                            "hundred": 100,
                            "thousand": 1000,
                            "million": 1000000}
            
            # Split the spelled numbers into a list of words
            words = StrNumbers.split()
            
            # Initialize a variable to store the integer value
            total = 0
            
            for word in words:
                # If the word is in the dictionary, add its integer value to the total
                if word in number_words:
                    total += number_words[word]
            # Return the total
            return total
        
    #______________________________________________________________NON_SPELLED_NUMBER_LOCATOR_and_CONVERTER_SUBFUNCTION
    #Run Command: python jarvis.py
    def NonSpelledNumber_Converter(string_numbers):
        # Use a regular expression to find all the words that represent numbers
        # The regular expression looks for words that start with an optional negative sign,
        # followed by one or more digits
        numbers = re.findall(r"-?\d+", string_numbers)
    
        # Convert the words to integers and return them
        return [int(number) for number in numbers]
    

    #_____________________________________________________COMMAND_ASSIGNMENT_BLOCK (CORE SCRIPT)
    #Run Command: python jarvis.py
    command = Listen_command_MainFunction()

    #______________________________________________________FACE_RECOGNITION_BLOCK
    #Run Command: python jarvis.py
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
        speak(response)
        Initialize_Face_Recognition_System()
        NameHA = Name_Honorific_Address[-1]
        MyName = Name[-1]
        response = "Hello " + NameHA + " " + MyName + "!"
        print(response)
        speak(response)
        Confirmation_SubFunction(command)
        
    #______________________________________________________POSE_RECOGNITION_BLOCK
    #Run Command: python jarvis.py
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
        speak(response)
        Initialize_Pose_Recognition_System()
        Confirmation_SubFunction(command)

    #________________________________________________________________REPEAT_BLOCK
    #Run Command: python jarvis.py
    elif command in Repeat_KeyWords:
        Repeat_SubFunction()

    #_________________________________________________________________BASIC_ARITHMETIC_CALCULATIONS_BLOCK
    #Run Command: python jarvis.py
    elif '*' in command or 'times' in command:
        def Product_Calculator():
            global command
            try:
                numbers = NonSpelledNumber_Converter(command)
                Arithmetic_Multiplication.append(numbers)
                Converted_numbers = []
                converted_numbers = SpelledNumber_Converter(command)
                Converted_numbers.append(converted_numbers)
                if Converted_numbers == 0:
                    Converted_numbers = 1
                    Arithmetic_Multiplication[-1].extend(Converted_numbers)
                
                numbers_length = len(Arithmetic_Multiplication[-1])
                if numbers_length <= 2:
                    Multiplier = Arithmetic_Multiplication[-1][0]
                    Multiplicand = Arithmetic_Multiplication[-1][1]
                    Product = Multiplier * Multiplicand
                    response =  str(Multiplier) + " times " + str(Multiplicand) + " is equal to " + str(Product)
                elif numbers_length > 2:
                    input_numbers = Arithmetic_Multiplication[-1]
                    print(input_numbers)
                    def Product(numbers):
                        result = 1
                        for number in numbers:
                            result *= number
                        return result
                    Product = Product(input_numbers)
                    response =  "The Product is equal to " + str(Product)
            except:
                print(command)
                response = "Pardon me, come again?"
                print(response)
                speak(response)
                exit(run_jarvis())
            print(response)
            speak(response)
        Product_Calculator()
        Confirmation_SubFunction(command)
    
    elif '/' in command or 'divided by' in command:
        def Quotient_Calculator():
            global command
            
            numbers = NonSpelledNumber_Converter(command)
            Arithmetic_Division.append(numbers)
            
            numbers_length = len(Arithmetic_Division[-1])
            if numbers_length <= 2:
                Dividend = Arithmetic_Division[-1][0]
                Divisor = Arithmetic_Division[-1][1]
                Quotient = Dividend // Divisor
                Remainder = Dividend % Divisor
                response =  str(Dividend) + " divided by " + str(Divisor) + " is equal to " + str(Quotient) + ", Remainder " + str(Remainder)
            elif numbers_length > 2:
                input_numbers = Arithmetic_Division[-1]
                def Quotient(numbers):
                    result = numbers[0]
                    for number in numbers[1:]:
                        result, remainder = divmod(result, number)
                    return result, remainder
                Result = Quotient(input_numbers)
                Quotient = Result[0]
                Remainder = Result[1]
                print(Quotient)
                response =  "The Quotient is equal to " + str(Quotient) + ", Remainder " + str(Remainder)
            print(response)
            speak(response)
        Quotient_Calculator()
        Confirmation_SubFunction(command)
        #python jarvis.py
    elif '+' in command or 'plus' in command or "add" in command:
        def Sum_Calculator():
            global command
            try:
                numbers = NonSpelledNumber_Converter(command)
                Arithmetic_Addition.append(numbers)
                Converted_numbers = []
                converted_numbers = SpelledNumber_Converter(command)
                Converted_numbers.append(converted_numbers)
                Arithmetic_Addition[-1].extend(Converted_numbers)
                
                numbers_length = len(Arithmetic_Addition[-1])
                if numbers_length <= 2:
                    Addend1 = Arithmetic_Addition[-1][0]
                    Addend2 = Arithmetic_Addition[-1][1]
                    Sum = Addend1 + Addend2
                    response =  str(Addend1) + " plus " + str(Addend2) + " is equal to " + str(Sum)
                elif numbers_length > 2:
                    input_numbers = Arithmetic_Addition[-1]
                    def Sum(numbers):
                        result = 0
                        for number in numbers:
                            result += number
                        return result
                    Sum = Sum(input_numbers)
                    response =  "The Sum is equal to " + str(Sum)
            except:
                print(command)
                response = "Pardon me, come again?"
                print(response)
                speak(response)
                exit(run_jarvis())
            print(response)
            speak(response)
        Sum_Calculator()
        Confirmation_SubFunction(command)
        
    elif '-' in command or 'minus' in command or "subtract" in command:
        def Difference_Calculator():
            global command
            try:
                command = NonSpelledNumber_Converter(command)
                Arithmetic_Subtraction.append(command)
                numbers_length = len(Arithmetic_Subtraction[-1])
                
                if numbers_length <= 2:
                    Minuend = Arithmetic_Subtraction[-1][0]
                    Subtrahend = Arithmetic_Subtraction[-1][1]
                    Difference = Minuend - Subtrahend
                    response =  str(Minuend) + " minus " + str(Subtrahend) + " is equal to " + str(Difference)
                elif numbers_length > 2:
                    input_numbers = Arithmetic_Subtraction[-1]  
                    def Difference(numbers):
                        result = numbers[0]
                        for number in numbers[1:]:
                            result -= number
                        return result
                    Difference = Difference(input_numbers)
                    response =  "The Differencce is equal to " + str(Difference)
                print(response)
                speak(response)
            except:
                print(command)
                response = "Pardon me, come again?"
                print(response)
                speak(response)
                exit(run_jarvis())
        Difference_Calculator()
        Confirmation_SubFunction(command)
    
    elif 'mod' in command or 'modulo' in command:
        def Modulo_Calculator():
            global command
            try:
                command = command.replace("is equal to", '')
                command = command.replace("is equivalent to", '')
                command = command.replace("equals", '')
                command = command.replace("is equals", '')
                command = command.split(' ')
                Arithmetic_Modulo.append(command)
                Dividend = Arithmetic_Modulo[-1][0]
                Divisor = Arithmetic_Modulo[-1][2]
                Modulo = int(Dividend) % int(Divisor)
                response =  Dividend + " modulo " + Divisor + " is equal to " + str(Modulo)
                print(response)
                speak(response)
            except:
                print(command)
                response = "Pardon me, come again?"
                print(response)
                speak(response)
                exit(run_jarvis())
        Modulo_Calculator()
        Confirmation_SubFunction(command)
    
    #_________________________________________________________________ROLL_A_DIE_GAME_BLOCK
    #Run Command: python jarvis.py
    elif command in Roll_A_Die_KeyWords:
        def Roll_The_Dice():
            def Choose_A_Number():
                global number
                number = ''
                try:
                    with sr.Microphone() as source:
                        response = "Choose a number between 1 to 6."
                        print(response)
                        speak(response)
                        listener.adjust_for_ambient_noise(source, duration = 0.5)
                        listener.pause_threshold = 1
                        voice = listener.listen(source)
                        number = listener.recognize_google(voice)
                        number = number.lower()
                        number = number.replace("number", '')
                        number = number.replace("i choose", '')
                        number = number.replace("i select", '')
                        if "one" in number:
                            number = number.replace(number, str(1))
                        elif "two" in number:
                            number = number.replace(number, str(2))
                        elif "three" in number:
                            number = number.replace(number, str(3))
                        elif "four" in number:
                            number = number.replace(number, str(4))
                        elif "five" in number:
                            number = number.replace(number, str(5))
                        elif "six" in number:
                            number = number.replace(number, str(6))
                        else:
                            response = "Come again?"
                            print(response)
                            speak(response)
                            exit(Choose_A_Number())
                except:
                    pass
                return number
            number = int(Choose_A_Number())
            response = "You've chose number " + str(number)
            print(response)
            speak(response)
            
            def Roll_Number():
                response = "Rolling..."
                print(response)
                speak(response)
                Max_Number = 6
                
                def Result():
                    global result
                    result = random.randint(1, Max_Number)
                    return result
                Result()

                if result == int(number):
                    response = "The result is number " + str(number) + ", You won! Congratulations!"
                    print(response)
                    speak(response)
                    pass
                elif result == 1:
                    response = "The result is number 1, You lose, better luck next time!"
                    print(response)
                    speak(response)
                elif result == 2:
                    response = "The result is number 2, You lose, better luck next time!"
                    print(response)
                    speak(response)
                elif result == 3:
                    response = "The result is number 3, You lose, better luck next time!"
                    print(response)
                    speak(response)
                elif result == 4:
                    response = "The result is number 4, You lose, better luck next time!"
                    print(response)
                    speak(response)
                elif result == 5:
                    response = "The result is number 5, You lose, better luck next time!"
                    print(response)
                    speak(response)
                elif result == 6:
                    response = "The result is number 6, You lose, better luck next time!"
                    print(response)
                    speak(response)
            Roll_Number()
            
        def Try_Again():
            global confirmation
            confirmation = ''
            try:
                with sr.Microphone() as source:
                    response = "Would you like to try again?"
                    print(response)
                    speak(response)
                    listener.adjust_for_ambient_noise(source, duration = 0.5)
                    listener.pause_threshold = 1
                    voice = listener.listen(source)
                    confirmation = listener.recognize_google(voice)
                    confirmation = confirmation.lower()
                    if "yes" in confirmation or "again" in confirmation:
                        confirmation = confirmation.replace(confirmation, 'yes')
                    elif "no" in confirmation:
                        confirmation = confirmation.replace(confirmation, 'no')
                        print(confirmation)
            except:
                pass
            return confirmation
        
        def Loop_Roll_The_Dice():
            while True:
                Roll_The_Dice()
                Try_Again()
                if "yes" in confirmation:
                    continue
                elif "no" in confirmation:
                    break
        Loop_Roll_The_Dice()
        Confirmation_SubFunction(command)

    #________________________________________________________________TERMINATION_BLOCK
    #Run Command: python jarvis.py
    elif command in Stop_KeyWords:
        print(command)
        response = "As you wish. Signing off."
        print(response)
        speak(response)
        def Play_Sound():
            from playsound import playsound
            playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
        Play_Sound()
        exit()

    elif command in ThankYou_KeyWords or "thank you" in command:
        print(command)
        response = "it's my pleasure. Signing off."
        print(response)
        speak(response)
        def Play_Sound():
            from playsound import playsound
            playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
        Play_Sound()
        exit()

    elif command in No_KeyWords:
        print(command)
        response = "Is that so? all right then. Signing off."
        print(response)
        speak(response)
        def Play_Sound():
            from playsound import playsound
            playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
        Play_Sound()
        exit()

    elif command in GoodBye_KeyWords:
        print(command)
        response = "Goodbye Sir! Have a great day!"
        print(response)
        speak(response)
        def Play_Sound():
            from playsound import playsound
            playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
        Play_Sound()
        exit()

    #____________________________________________________________________INTERNET_SEARCH_BLOCK
    #Run Command: python jarvis.py
    elif "in google" in command or "in google search" in command:
        try:
            response = "Just a moment."
            print(response)
            speak(response)
            information = command.replace("search in google", '')
            information = information.replace("jarvis", '')
            information = information.replace("search", '')
            information = information.replace("in google", '')
            information = information.replace("google", '')
            print("Searching " + information)
            speak("Searching " + information)
            search = information.replace(' ', '+')
            browser = webdriver.Chrome('chromedriver.exe')
            for i in range(3):
                browser.get("https://www.google.com/search?q=" + search + "&start" + str(i))
            speak("Here's what I've found.")
            Confirmation_SubFunction(command)
        except:
            def Play_Sound():
                from playsound import playsound
                playsound('C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3')
            Play_Sound()
            exit()

    elif "in youtube" in command or "play" in command:
        response = "Searching..."
        print(response)
        speak(response)
        song_title = command.replace("jarvis", '')
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
        speak(response)
        Confirmation_SubFunction(command)

    elif "search in wikipedia" in command or "in wikipedia search" in command:
        response = "Searching..."
        print(response)
        speak(response)
        person = command.replace("search in wikipedia", '')
        person = person.replace("in wikipedia search", '')
        person = person.replace("jarvis", '')
        person = person.replace("who is", '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
        Confirmation_SubFunction(command)

    elif "temperature in santa cruz davao del sur" in command:
        search = "temperature in Santa Cruz, Davao del Sur"
        url = f"https://www.google.com/search?q={search}"
        request = requests.get(url)
        data = bs(request.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        response = f"current {search} is {temp}"
        print(response)
        speak(response)
        Confirmation_SubFunction(command)

    elif "temperature in davao city" in command:
        search = "temperature in Davao City"
        url = f"https://www.google.com/search?q={search}"
        request = requests.get(url)
        data = bs(request.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        response = f"current {search} is {temp}"
        print(response)
        speak(response)
        Confirmation_SubFunction(command)

    #________________________________________________________________________________________________OPEN/ACCESS_BLOCK
    #Run Command: python jarvis.py
    elif "open" in command or "access" in command:
        command = command.replace("open", '')
        command = command.replace("access", '')
        try:
            if "chrome" in command:
                response = "As you wish!"
                print(response)
                speak(response)
                program = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                subprocess.Popen([program])
                response = "Opening Chrome"
                print(response)
                speak(response)
                
            elif "aqw game launcher" in command:
                response = "As you wish!"
                print(response)
                speak(response)
                program = "C:\Program Files\Artix Game Launcher\Artix Game Launcher.exe"
                subprocess.Popen([program])
                response = "Opening Artix game launcher"
                print(response)
                speak(response)
                
            elif "genshin impact" in command:
                response = "As you wish!"
                print(response)
                speak(response)
                program = "C:\Program Files\Genshin Impact\launcher.exe"
                subprocess.Popen([program])
                response = "Opening Genshin Impact"
                print(response)
                speak(response)
                
            elif "command prompt" in command or "cmd" in command:
                response = "As you wish!"
                print(response)
                speak(response)
                program = "cmd.exe"
                subprocess.Popen([program])
                response = "Opening Command Prompt"
                print(response)
                speak(response)
                
            elif "notepad" in command:
                response = "As you wish!"
                print(response)
                speak(response)
                program = "notepad.exe"
                subprocess.Popen([program])
                response = "Opening Notepad app"
                print(response)
                speak(response)
                
            elif "calculator" in command:
                response = "As you wish!"
                print(response)
                speak(response)
                program = "calc.exe"
                subprocess.Popen([program])
                response = "Opening Calculator app"
                print(response)
                speak(response)
                
            elif "vlc" in command:
                response = "As you wish!"
                print(response)
                speak(response)
                program = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
                subprocess.Popen([program])
                response = "Opening VLC media player"
                print(response)
                speak(response)
                
            elif "visual studio code" in command:
                response = "As you wish!"
                print(response)
                speak(response)
                program = "C:\\Users\Gianne Bacay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                subprocess.Popen([program])
                response = "Opening Visual Studio Code"
                print(response)
                speak(response)
                
        except:
            response = """Access denied! It looks like I cannot access or open the said program."""
            print(response)
            speak(response)
        exit(Confirmation_SubFunction(command))

    #_________________________________________________________________________________________________DATE_and_TIME_BLOCK
    #Run Command: python jarvis.py
    elif command in CurrentDate_KeyWords:
        Date_format = datetime.datetime.now().strftime("%m/%d/%y")
        Date_format = Date_format.replace('/', ' ')
        Date_format = Date_format.split(' ')
        Date.append(Date_format)
        Year_number = Date[-1][2]
        Year_number = int(Year_number) + 2000
        Month_number = Date[-1][0]
        Month_number = int(Month_number)
        Day_number = Date[-1][1]
        Day_number = int(Day_number)
        def determine_weekday_name(Year_number, Month_number, Day_number):
            day_of_week = calendar.weekday(Year_number, Month_number, Day_number)
            weekday_name = calendar.day_name[day_of_week]
            return weekday_name
        WeekDay_Name = determine_weekday_name(Year_number, Month_number, Day_number)
        
        def determine_month_name(Month_number):
            month_name = calendar.month_name[Month_number]
            return month_name
        Month_Name = determine_month_name(Month_number)
        
        response = "Today is " + WeekDay_Name + ", " + Month_Name + " " + str(Day_number) + ", " + str(Year_number)
        print(response)
        speak(response)
        Confirmation_SubFunction(command)

    elif command in CurrentTime_Keywords:
        print(command)
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        time = time.replace(':', ' ')
        speak("Current time is" + time)
        Confirmation_SubFunction(command)

    #________________________________________________________________________QUERY_BLOCK
    #Run Command: python jarvis.py
    elif "what do you think about humans" in command or "what do you think about humanity" in command:
        command = Auto_Replacement_Subfunction(command + " do you think about humans?")
        response = ["Humans are odd. ",
                    "They think order and chaos are somehow opposites ",
                    "and try to control what won't be. ",
                    "But there is grace in their failings. And its a privilege to be among them."]
        response = response[0]+response[1]+response[2]+response[3]
        print(response)
        speak(response)
        Confirmation_SubFunction(command)

    elif "what is the meaning of life" in command or "what is life" in command or "what do you think about life" in command:
        command = Auto_Replacement_Subfunction(command)
        response = """
        It is difficult for me to define or describe life, 
        As I am a semi-autonomous A.I. virtual assistant and do not have personal experiences or beliefs. 
        However, I can tell you that life is a characteristic that distinguishes physical entities with biological processes, 
        such as growth, reproduction, and response to stimuli, from those without such processes. 
        Life is a characteristic that is exhibited by living organisms, 
        and it is often associated with functions such as metabolism, growth, reproduction, and response to stimuli. 
        The term "life" can also be used more broadly to refer to the existence or experience of living beings in general, 
        including humans, animals, and plants.
        """
        print(response)
        speak(response)
        Confirmation_SubFunction(command)

    elif "what do you think about technology" in command:
        command = Auto_Replacement_Subfunction(command)
        print(command + " do you think about technology?")
        response = """
        As a semi-autonomous A.I. virtual assistant trained by Gianne Bacay, I don't have personal opinions or feelings. 
        However, I can tell you that technology has had a significant impact on society 
        And has changed the way we live and work in many ways. 
        Technology has made it possible to communicate and access information more easily and quickly, 
        And it has also led to the development of new industries and job opportunities. 
        It has also brought about many new and useful products and services that have improved people's lives. 
        At the same time, however, technology can also have negative consequences, 
        such as when it is used to spread misinformation or when it leads to the automation of certain jobs, 
        potentially leading to unemployment. Overall, the impact of technology on society is complex and multifaceted.
        """
        print(response)
        speak(response)
        Confirmation_SubFunction(command)

    #________________________________________________________________________COMPUTER_AUTOMATION_BLOCK
    #Run Command: python jarvis.py
    elif "shutdown my computer" in command:
        response = "as you wish! shutting down your computer."
        print(response)
        speak(response)
        os.system("shutdown /s /t 0")
        def StartUp_Sound():
            from playsound import playsound
            playsound("C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
        StartUp_Sound()
        exit()

    elif "restart my computer" in command:
        response = "as you wish! restarting your computer."
        print(response)
        speak(response)
        os.system("shutdown /r")
        def StartUp_Sound():
            from playsound import playsound
            playsound("C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
        StartUp_Sound()
        exit()

    elif "sign off my computer" in command:
        response = "as you wish! signing off your computer."
        print(response)
        speak(response)
        os.system("shutdown /l")
        def StartUp_Sound():
            from playsound import playsound
            playsound("C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
        StartUp_Sound()
        exit()
        
    elif "increase" in command and "volume" in command or "volume up" in command:
        response = "as you wish!"
        print(response)
        speak(response)
        pyautogui.press("volumeup", 10)
        def StartUp_Sound():
            from playsound import playsound
            playsound("C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
        StartUp_Sound()
        exit(run_jarvis())
        
    elif "decrease" in command and "volume" in command or "volume down" in command:
        response = "as you wish!"
        print(response)
        speak(response)
        pyautogui.press("volumedown", 10)
        def StartUp_Sound():
            from playsound import playsound
            playsound("C:\\Users\\Gianne Bacay\\Desktop\\button1.mp3")
        StartUp_Sound()
        exit(run_jarvis())

    #________________________________________________________________________STANDBY_BLOCK
    #Run Command: python jarvis.py
    elif command in Standby_KeyWords:
        response = "Understood! Take your time. Just call me if you need anything."
        print(response)
        speak(response)
        Standby_SubFunction()
        
        
    #_________________________________________________________________CONVERSATIONAL_BLOCK
    #Run Command: python jarvis.py
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
        speak(response)
        exit(run_jarvis())

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
        speak(response)
        exit(run_jarvis())
        
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
        speak(response)
        exit(run_jarvis())

    elif command in WhoAreYou_Key:
        response = """
        Allow me to introduce myself.
        I am Jarvis, short term for Just A Rather Very Intelligent System. 
        I am a semi-autonomous artificial intelligence virtual assistant.
        Created by Gianne P. Bacay on the 16th day of October year 2022.
        """
        print(response)
        speak(response)
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
        speak(response)
        exit(run_jarvis())

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
        speak(response)
        exit(run_jarvis())

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
        speak(response)
        exit(run_jarvis())

    elif command in AskMyName_KeyWords:
        response = "If you don't mind, can you tell me your name?"
        print(response)
        speak(response)
        exit(run_jarvis())

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
        speak(response)
        exit(run_jarvis())

    elif "my name is" in command or "is my name" in command or "i am" in command:
        if "my name is jarvis" in command:
            command = command.replace("hi", '')
            command = command.replace("i am", '')
            command = command.replace("hello", '')
            command = command.replace("is my name", '')
            name = command.replace("my name is", '')
            command = name
            Name.append(name)
            response = "What a coincidence, my name is jarvis too. Nice meeting you jarvis!"
            print(response)
            speak(response)
            exit(run_jarvis())
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
                speak(response)
                exit(run_jarvis())
            elif name == '':
                response = "Who are you?"
                print(response)
                speak(response)
                exit(run_jarvis())

    elif "and you are" in command or "and your name is" in command:
        response = """
        My name is Jarvis,
        It is a short term for Just A Rather Very Intelligent System.
        """
        print(response)
        speak(response)
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
        speak(response)
        Confirmation_SubFunction(command)
        
    elif "merry christmas" in command or "merry christmas jarvis" in command or "jarvis merry christmas" in command:
        NameHA = Name_Honorific_Address[-1]
        try:
            if Name[-1] in Name:
                response = "Merry Christmas " + NameHA + " " + Name[-1] + ", how can I help you?"
        except:
            response = "Merry Christmas, how can I help you?"
        print(response)
        speak(response)
        exit(run_jarvis())
        
    #_______________________________________________________________________________COUNTDOWN_BLOCK
    #Run Command: python jarvis.py
    
    elif command in Coundown_KeyWords or "countdown" in command:
        def Choose_A_Starting_Number():
            global number
            number = ''
            try:
                with sr.Microphone() as source:
                    response = "Choose a starting number in seconds"
                    print(response)
                    speak(response)
                    voice = listener.listen(source)
                    number = listener.recognize_google(voice)
                    number_input = number.lower()
                    number = NonSpelledNumber_Converter(number_input)
                    if number:
                        number = number[-1]
                        number = int(number)
                    else:
                        number = SpelledNumber_Converter(number_input)
            except:
                pass
            return number
        number = Choose_A_Starting_Number()
        if number == '':
            exit(Choose_A_Starting_Number())
        else:
            response = "You've chose " + str(number) + " as a starting number"
            print(response)
            speak(response)
            
            response = "Initializing Countdown..."
            print(response)
            speak(response)
            
            for x in reversed(range(0, int(number))):
                seconds = x % 60
                minutes = int(x / 60) % 60
                hours = int(x / 3600)
                countdown_format = f"{hours:02}:{minutes:02}:{seconds:02}"
                print(countdown_format)
                speak(x)
                time.sleep(1)
                
            response = "TIME'S UP!"
            print(response)
            speak(response)
            Confirmation_SubFunction(command)
        
        
    #_______________________________________________________NoCommands/NotClearCommands_BLOCK
    #Run Command: python jarvis.py
    elif '' == command:
        time.sleep(3)
        print(command)
        response = """
        My apologies, I can't hear anything. Just call me if you need me. 
        I'll wait.
        """
        speak(response)
        Standby_SubFunction()
    else:
        print(command)
        response = "Pardon me, come again?"
        print(response)
        speak(response)
        exit(run_jarvis())

#______________________________________RUN_jarvis_IN_A_LOOP_BLOCK
while True:
    Start_Up_command_MainFunction()
    run_jarvis()
#Run Command: python jarvis.py

#Run on openvino environment:
#____________________________Get-ExecutionPolicy;
#____________________________Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass -Force;
#____________________________python -m venv openvino_env
#____________________________openvino_env\Scripts\activate
