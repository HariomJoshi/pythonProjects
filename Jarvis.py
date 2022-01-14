import datetime
import time
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import vlc
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
# this can also be done as follows
# engine.setProperty('voice', engine.getProperty('voices')[0].id)


def speak(audio):
    '''speaks the argument given to it'''
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    '''gives normal salutation, with respect to time'''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am jarvis, How may I help you?")

def takeCommand():
    '''take input from microphone and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Not able to recognize")
        return "None"
    return query


def send_mail(Receiver_email, subject, body):
    '''send mail to Reciever_email with subject:subject and body:body'''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('goodhariom@gmail.com', 'mguxhvmcsqsukcwk')
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail("goodhariom@gmail.com", Receiver_email, msg)
    server.quit()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        # following are the logic of tasks based on querry
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            time.sleep(0.5)
            speak("do you want to open the wikipedia page?")
            inp = takeCommand().lower()
            if 'yes' in inp:
                res = wikipedia.page(query)
                url = res.url
                webbrowser.open(url)
            # add do you want to open wikipedia page for in the browser?
            # .url function might be helpful

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open('google.com')

        elif 'open music' in query:
            speak("opening youtube music")
            webbrowser.open('music.youtube.com')

        elif 'open stack overflow' in query:
            speak("opening stack overflow")
            webbrowser.open('stackoverflow.com')

        elif 'play don\'t breathe' in query:
            speak("playing don\'t breathe")
            dir = 'D:\\movies\\DontBreathe1'
            series = os.listdir(dir)
            print(series)
            media = vlc.MediaPlayer(f"{dir}\\{series[0]}")
            media.play()

        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir, the time is {time}")

        elif 'open code' in query:
            # following path is copied from    VScode file location -> properties -> target
            codepath = "C:\\Users\\hariom\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            speak("Type the email you want to send email to")
            sendto = input("Email to: ")
            speak("What should be the subject?")
            print("Subject: ", end="")
            subject = takeCommand().upper()
            speak("What should be the body? ")
            print("Body: ", end="")
            body = takeCommand().lower()
            speak("Sending mail")
            send_mail(sendto, subject, body)
            speak("Mail sent")

        elif 'perfect' in query:
            speak("I am perfect, but not as perfect as you!")

        elif 'quit' in query:
            speak("quitting")
            break


