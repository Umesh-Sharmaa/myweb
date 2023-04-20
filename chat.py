import datetime
import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
openai.api_key = "YOUR API KEY"


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)
tm=int(datetime.datetime.now().hour)

def greet():
    if tm>=0 and tm<12:
      engine.say("Good morning sir")
      engine.runAndWait()

    elif tm>=12 and tm<16:
        engine.say("Good afternoon sir")
        engine.runAndWait()

    elif tm>=16 and tm<20:
        engine.say("Good evening sir")
        engine.runAndWait()

    elif tm>=20 and tm<=24:
        engine.say("Good night sir")
        engine.runAndWait()


def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")
      r.energy_threshold=400
      r.pause_threshold=1
      audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"you said {query}")
        return query

    except Exception:
          print("say that again please....")
          take_command()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000,
    )
    answer = response.choices[0]['text']
    return answer


if __name__=='__main__':
    greet()
    while True:
        
        work=str(take_command()).lower()

        if 'hello' in work:
            speak("Hello sir, how may i help you")

        elif 'go to sleep' in work:
            speak("Sure sir, Have a nice day!!")
            break
        
        elif 'on youtube' in work:
            work=work.replace("on youtube","")
            speak("Sure sir..,here you go")
            webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={work}')

        elif 'open youtube' in work:
            speak("Sure sir..,here you go")
            webbrowser.open_new_tab('https://www.youtube.com/')

        elif 'on google' in work:
            speak("Sure sir..,here you go")
            work=work.replace("on google","")
            webbrowser.open_new_tab(f'https://www.google.com/search?q={work}')

        else:
         answer = generate_text(work)
         speak(answer)
         print(answer)
        
        # else:
        #     speak("Sorry, can you say that again?")
        #     continue