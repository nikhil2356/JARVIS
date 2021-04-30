import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os.path
import smtplib
import random
import pass1
import pyjokes



# voice selection for jarvis
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# voices is a list of voices on your computer
engine.setProperty('voice', voices[1].id)


# speak function will take string input and speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# wishMe() function will greet you whenever you run this script
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
        speak("Hope everything good in last night")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
        speak("Hope everything was fine in morning")

    else:
        speak("Good Evening sir")
        speak("Hope everything was fine Afternoon")

    speak("I am jarvis sir designed for my boss Pranadeep. Tell me sir  how can i help you?")


# jarvis will take your voice command and convert into string
def takeCommand():
    # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing sir...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said; {query}\n")

    except Exception as e:
        print(e)
        speak("Say That Again sir...")
        return "None"

    return query


# jarvis will send email and please make sure to make your gmail account less secure.
def sendEmail(to, content):
    e = pass1.getEmail()
    p = pass1.getPass()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(e, p)
    server.sendmail(e, to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query

        if 'according to wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('according to wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # --------------jarvis for opening youtube--------------
        elif 'open youtube' in query:
            speak('opening youtube..')
            webbrowser.open("youtube.com")

        # ------------------jarvis for opening notepad------------
        elif 'open notepad' in query:
            rpath = "C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.exe"
            os.startfile(rpath)

        #  ------------------jarvis for opening command prompt---------------
        elif 'open command prompt' in query:
            os.system("start cmd")

        # --------------------jarvis for telling a joke-----------------------
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # --------------------jarvis for shutdown----------------------------

        elif 'shut down the system' in query:
            os.system("shutdown /s /t S")


        # -----------------------jarvis to open google------------------------
        elif 'open google' in query or 'open chrome' in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'according to google' in query:
            speak('opening google..')
            query = query.replace('according to google', '')
            webbrowser.open("http://google.com/#q=" + query, new=2)

        elif 'open facebook' in query:
            speak('opening facebook sir..')
            webbrowser.open("facebook.com")

        elif 'open github' in query:
            speak('opening github..')
            webbrowser.open("github.com")

        elif 'where am i' in query or 'where we are' in query or 'Track me' in query:
            speak("wait sir , let me check")
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif 'play music' in query:
            music_dir = "C:\\Users\\hites\\OneDrive\\Desktop\\music"
            songs = os.listdir(music_dir)
            n = len(songs)
            index = random.randint(0, n)
            os.startfile(os.path.join(music_dir, songs[index]))





        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'include' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)


        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        elif 'jarvis are you there' in query:
            speak('yes sir, I am at your service')

        elif 'what is your name' in query:
            speak('My name is JARVIS')
            speak('JARVIS stands for JUST A RATHER VERY INTELLIGENT SYSTEM')

        elif 'can i see your code' in query:
            speak('sorry sir ,code cannot  be accessed')
            speak('but i can give u company')

        elif 'do you know google assistant' in query or 'do you know siri' in query:
            speak('These are just like me created by someone for their assistant')

        elif 'do you know emotions' in query:
            speak('I cannot do it, but i know all emotions which humans can do ')

        elif 'do you get angry on me' in query:
            speak("No sir ,i don't get angry on you,i am your assistant,but i get angry on your sister")

        elif 'do you know my sister' in query:
            speak('I know all your family members')



        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,the time is {strTime}")

        elif 'open editor' in query:
            speak('opening sublime text editor sir..')
            path = "C:\\Users\\hites\\OneDrive\\Desktop\\Sublime Text 3\\sublime_text.exe"
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak("What should i say sir?")
                content = takeCommand()
                to = "panyalasaipriya123@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry Pranadeep sir,I am not able to send this email,try again sir")


        elif "who are you" in query:
            speak("I am jarvis sir, I an your assistant")
            speak("Designed by Pranadeep My boss")

        elif "what can you do for me" in query:
            speak("Sir i can do many things sir such i can open notepad,command prompt, i can send mail , i can also open youtube google instagram,facebook and many more sir " )

        elif 'how are you' in query:
            speak("I am fine sir, Thank you sir")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine sir")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening sir")
            a = int(takeCommand())
            print(a)
        elif 'Do you know Saipriya' in query or "SaiPriya" in query:
            speak("Sailoooo")


        elif 'close jarvis' in query:
            speak('goodbye sir, have nice day sir')
            exit()