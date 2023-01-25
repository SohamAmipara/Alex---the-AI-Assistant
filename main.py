'''ALEX AI ASSISTANT'''


'''import required libraries'''
import pyttsx3     # using pyttsx3 we convert text data into speech
import datetime     
import speech_recognition as sr     # using speech_recognition we take input from mic as a speech and convert it into text
import smtplib     # built in library in python for the use of send the email
from secretsSecurity import senderMail,sendMailPassword,to
from email.message import EmailMessage  
import pyautogui     # using pyautogui for enter the whatsapp message
import webbrowser as wb     # used for open webbrowser for whatsapp and other
from time import sleep 
import wikipedia     # used for searching something from the wikipedia
import pywhatkit     # used for youtube
import requests
from newsapi import NewsApiClient     # used fro get the news
import clipboard
import os
import pyjokes     # used for a jokes
import time as tt
import string
import random
import psutil
from nltk.tokenize import word_tokenize     # NLP libraries for good result


'''text data into speech'''
engine = pyttsx3.init()     # using this we called a initial function which is on pyttsx3

# engine.say('Hello Sir, This is Alex 1.0.')
# engine.runAndWait()


'''take user input as a text and convert it into speech'''
def speak(audio):     # define speak function
    engine.say(audio)
    engine.runAndWait()

# while True:     # use while true for take input continuously 
#     audio = input('Enter the text to convert it into the speech: \n')
#     speak(audio)


'''set voice Male or Female'''
def getVoices(voice):     # define getVoice function
    voices = engine.getProperty('voices')
    # print(voices[0].id) # Male voice - HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
    # print(voices[1].id) # Female Voice - HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0

    if voice == 1:
        engine.setProperty('voice',voices[0].id)
        # speak('Hello Sir, This is Alex 1.0')
    if voice == 2:
        engine.setProperty('voice',voices[1].id)
        # speak('Hello Sir, This is Jenny 1.0')


# while True:
#     voice = int(input('Press 1 for Male Voice\nPress 2 for Female Voice\n'))
#     getVoices(voice)


'''time and date'''
def time():     # define time function
    time = datetime.datetime.now().strftime('%I:%M:%S')     # Hour-I, Minutes-M, Seconds-S
    speak('The current time is ')
    speak(time)

# time()

def date():     # define date function
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak('The current Date is ')
    speak(date)
    speak(month)
    speak(year)

# date()


'''greeting and wishme'''
def greeting():     # define greeting function
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak('Good Morning!')
    if hour >=12 and hour<18:
        speak('Good Afternoon!')
    if hour >=18 and hour<24:
        speak('Good Evening!')

def wishMe():     # define wishMe function
    speak('Welcome Back Sir!')
    greeting()
    speak('Alex at your service, Please tell me how can I help you!?')
    # speak('Jenny at your service, Please tell me how can I help you!?')

# wishMe()


'''take command CMD'''
def takeCommandCMD():     # define takeCommandCMD function
    query = input('Write your query for Alex: \n')
    return query


'''take command MIC'''
def takeCommandMIC():     # define takeCommandMIC function
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-IN')
        print(query)
    except Exception as e:
        print(e)
        speak('Say that again, Please...')
        return 'None'
    return query


'''send mail'''
def sendMail(receiver, subject, content):     # define sendMail function
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderMail ,sendMailPassword)
    # server.sendmail(senderMail, to, 'Hello this is a test mail from Alex.')
    # server.sendmail(senderMail, to, content)
    email = EmailMessage()
    email['From'] = senderMail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

# sendMail()


'''send whatsapp message'''
def sendWhatsappMessage(phone_no, message):     # define sendWhatsappMessage function
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')


'''search in wikipedia'''
def searchInWikipedia():     # define searchInWikipedia function
    speak('Searching on Wikipedia...')
    query = takeCommandMIC()
    result = wikipedia.summary(query, sentences = 2)
    print(result)
    speak(result)


'''search on google'''
def searchOnGoogle():     # define searchOnGoogle function
    speak('What shoud I search for!?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+search)


'''search on YouTube'''
def searchOnYouTube():     # define searchOnYouTube function
    speak('What should I search for on YouTube!?')
    topic = takeCommandMIC()
    pywhatkit.playonyt(topic)


'''weather'''
def weather():     # define weather function
    # city = 'surat'
    speak('What city do you want to know about the weather!?')
    city = takeCommandMIC()

    # url = 'http://api.openweathermap.org/data/2.5/weather?q=Pune&units=imperial&appid=bcbb9000adf5cc4d07198ae2f4cea22f'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=bcbb9000adf5cc4d07198ae2f4cea22f'
    
    req = requests.get(url)
    data = req.json()
    
    weather = data['weather'][0]['main']
    temp = data['main']['temp']
    temp = round((temp - 32) * 5/9)
    description = data['weather'][0]['description']
    
    print(weather)
    print(temp)
    print(description)

    speak(f'Weather in {city} city is like,..')
    speak('Temperature is {} degree celcius'.format(temp))
    speak('Weather is {}'.format(description))


'''get news from api'''
def getNews():     # define getNews function
    newsApi = NewsApiClient(api_key='{YOURAPI}')

    speak('What topic do you want to know about!?')
    topic = takeCommandMIC()

    data = newsApi.get_top_headlines(q=topic, language = 'en', page_size = 5)
    newsData = data['articles']
    
    for x,y in enumerate(newsData):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))

    speak("That's it for now, I'll update you in some time." )


'''read selected text'''
def text2speech():     # define text2speech function
    text = clipboard.paste()
    print(text)
    speak(text)


'''open vs code'''
def openVsCode():     # define openVsCode function
    codepath = '{YOURVSCODEPATH}'
    os.startfile(codepath)


'''open documents'''
def openDocuments():     # define openDocuments function
    os.system('explorer C://{}'.format(query.replace('Open','')))


# '''open downloads'''
# def openDownloads():     # define openDownloads function
#     os.system('explorer C://{}'.format(query.replace('Open','')))


# '''open pictures'''
# def openPictures():     # define openPictures function
#     os.system('explorer C://{}'.format(query.replace('Open','')))


# '''open desktop'''
# def openDesktop():     # define openDesktop function
#     os.system('explorer C://{}'.format(query.replace('Open','')))


'''jokes'''
def joke():     # define joke function
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


'''take a screenshot'''
def screenshot():     # define screenShot function
    nameImg = tt.time()
    nameImg = '{GIVEPATH}+{NAMEIMG}.png'
    img = pyautogui.screenshot(nameImg)
    img.show()


'''remember'''
def rememberThat():     # define rememberThat function     
    speak('What should I remember!?')
    data = takeCommandMIC()
    speak('You said me to remember that '+data)
    remember = open('data.txt','w')
    remember.write(data)
    remember.close()


'''do you know'''
def doYouKnow():     # define doYouKnow function
    remember = open('data.txt','r')
    speak('You told me to remember that '+remember.read())


'''password generator'''
def passwordGen():     # define passwordGen function
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 10

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newPass = (''.join(s[0:passlen]))
    print(newPass)
    speak(newPass)

 
'''cpu and battery update'''
def cpuBattery():     # define cpuBattery function
    usage = str(psutil.cpu_percent())
    speak('CPU is at '+usage)
    battery = psutil.sensors_battery()
    speak('Battery is at'+battery.percent)


'''main function'''
if __name__ == '__main__':     # define __main__ function
    getVoices(1)
    wishMe()
    # wakeword = 'Alex'
    while True:
        # query = takeCommandCMD().lower()
        query = takeCommandMIC().lower()
        query = word_tokenize(query)
        print(query)
        # if wakeword in query:

        if 'time' in query:     # time
            time()

        elif 'date' in query:     # date
            date()

        elif 'mail' in query:     # mail
            email_list = {
                'ABC':'abc123@gmail.com'
            }
            try:
                speak('To Whom you want to send the mail!?')
                name = takeCommandMIC().lower()
                receiver = email_list[name]
                speak('What is the subject of the mail!?')
                subject = takeCommandMIC()
                speak('What shoud I write!? \n')
                content = takeCommandMIC()
                sendMail(receiver, subject, content)
                speak('Email has been sent successfully.')
            except Exception as e:
                print(e)
                speak('Sorry!!! Unable to send the Email. Please, try again...')
        
        elif 'message' in query:     # whatsapp message
            username_list = {
                'ABC':'+(country code) 1234567890'
            }
            try:
                speak('To Whom you want to send the whatsapp message!?')
                username = takeCommandMIC().lower()
                phone_no = username_list[username]
                speak('What is the message!?')
                message = takeCommandMIC()
                sendWhatsappMessage(phone_no,message)
                speak('Message has been sent successfully.')
            except Exception as e:
                print(e)
                speak('Sorry!!! Unable to send the message. Please, try again...')
        
        elif 'wikipedia' in query:     # wikipedia
            searchInWikipedia()

        elif 'search' in query:     # google search
            searchOnGoogle()

        elif 'youtube' in query:     # youtube search
            searchOnYouTube()

        elif 'weather' in query:     # weather
            weather()

        elif 'news' in query:     # get news
            getNews()

        elif 'read' in query:     # text to speech
            text2speech()

        elif 'open vs code' in query:     # open vs code 
            openVsCode()

        elif 'open document' in query:     # open documents 
            openDocuments()

        # elif 'open downloads' in query:     # open downloads
        #     openDownloads()

        # elif 'open pictures' in query:     # open pictures 
        #     openPictures()
            
        # elif 'open desktop' in query:     # open desktop
        #     openDesktop()

        elif 'joke' in query:     # jokes
            joke()

        elif 'screenshot' in query:     # take a screenshot
            screenshot()

        elif 'remember that' in query:     # remember
            rememberThat()

        elif 'do you know anything' in query:     # do you know
            doYouKnow()

        elif 'password' in query:     # password generator
            passwordGen()

        elif 'cpu and battery' in query:     # cpu and battery update
            cpuBattery()

        elif 'offline' in query:     # Alex offline
            quit()