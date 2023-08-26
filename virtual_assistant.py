import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import subprocess
#import PyAudio



# hear the microphone and return the audio as text
def transform_audio_into_text():

    # store recognizer in variable
    r = sr.Recognizer()

    # set microphone
    with sr.Microphone() as source:

        # waiting time
        r.pause_threshold = 0.8

        # report that recording has begun
        print("You can now speak")

        # save what you hear as audio
        audio = r.listen(source)

        try:
            # search on google
            request = r.recognize_google(audio, language="en-us")

            # test in text
            print("You said " + request)

            # return request
            return request

        # In case it doesn't understand audio
        except sr.UnknownValueError:

            # show proof that it didn't understand the audio
            print("Ups! I didn't understand audio")


            # return error
            return "I am still waiting"

        # In case the request cannot be resolved
        except sr.RequestError:

            # show proof that it didn't understand the audio
            print("Ups! there is no service")

            # return error
            return "I am still waiting"

        # Unexpected error
        except Exception as e:

            # show proof that it didn't understand the audio
            print("Ups! something went wrong")
            print(f"Error details: {e}")

            # return error
            return "I am still waiting"


# Function so the assistant can be heard
def mac_speak(text):
    speak_cmd = f'say "{text}"'
    subprocess.call(speak_cmd, shell=True)


# Inform day of the week
def ask_day():

    # Create a variable with today information
    day = datetime.date.today()
    print(day)

    # Create variable for day of the week
    week_day = day.weekday()
    print(week_day)

    # Names of days
    calendar = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}

    # Say the day of the week
    mac_speak(f'Today is {calendar[week_day]}')


# Inform what time it is
def ask_time():

    # Variable with time information
    time = datetime.datetime.now()
    time = f'At this moment it is {time.hour} hours and {time.minute} minutes'

    print(time)

    # Say the time
    mac_speak(time)


# Create initial greeting
def initial_greeting():

    # Say greeting
    mac_speak('Hello I am Hazel. How can I help you?')


# Main function of the assistant
def my_assistant():

    # Activate the initial greeting
    initial_greeting()

    # Cut-off variable
    go_on = True

    # Main loop
    while go_on:

        # Activate microphone and save request
        my_request = transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            mac_speak('Sure, I am opening youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in my_request:
            mac_speak ('Of course, I am on it')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is today' in my_request:
            ask_day()
            continue
        elif 'what time it is' in my_request:
            ask_time()
            continue
        elif 'do a wikipedia search for' in my_request:
            mac_speak('I am looking for it')
            my_request = my_request.replace('do a wikipedia search for', '')
            answer = wikipedia.summary(my_request, sentences=1)
            mac_speak('according to wikipedia: ')
            mac_speak(answer)
            continue
        elif 'search the internet for' in my_request:
            mac_speak('of course, right now')
            my_request = my_request.replace('search the internet for', '')
            pywhatkit.search(my_request)
            mac_speak('this is what i found')
            continue
        elif 'play' in my_request:
            mac_speak('oh, what a great idea! I´ll play it right now')
            pywhatkit.playonyt(my_request)
            continue
        elif 'joke' in my_request:
            mac_speak(pyjokes.get_joke())
            continue
        elif 'stock price' in my_request:
            share = my_request.split()[-2].strip()
            portfolio = {'apple': 'APPL',
                         'amazon': 'AMZN',
                         'google': 'GOOGL'}
            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info['regularMarketPrice']
                mac_speak(f'I found it! The price of {share} is {price}')
                continue
            except:
                mac_speak('I am sorry, but I didn´t find it')
                continue
        elif 'goodbye' in my_request:
            mac_speak('I am going to rest. Let me know if you need anything')
            break


my_assistant()
