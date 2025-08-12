import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musiclibrary
import requests
import wikipedia  
from openai import OpenAI

recognizer=sr.Recognizer()
newskey="e1435f553b2348b49e532f43491ae115"

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160) 
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)
def aiprocess(command):
   client = OpenAI(api_key="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") 

   completion = client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": command}
    ],
    temperature=0.7
   )

   return (completion.choices[0].message.content)

    

def processcommand(c):
   if "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open github" in c.lower():
      webbrowser.open("https://github.com")
   elif c.lower().startswith("play"):
      song=c.lower().split(" ")[1]
      link="https://www.youtube.com/watch?v=JtBfBHfHWEg"
      webbrowser.open(link)  
   elif "how are you" in c.lower():
      speak("i am fine how's your day")  
   elif "news" in c.lower():
      r=requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={newskey}" ) 
      if r.status_code == 200:
         data = r.json()
         articles = data['articles']
         speak("BBC Top Headlines")
         for i, article in enumerate(articles):
            speak(f"{i+1}. {article['title']}")
   else:  
      try:                                                                         
         result = wikipedia.summary(c, sentences=2)
         speak(result)
      except wikipedia.exceptions.DisambiguationError as e:
         speak(f"That is too general. Did you mean {e.options[0]}?")
      except wikipedia.exceptions.PageError:
         speak("Sorry, I couldn't find anything related to that.")
      except Exception as e:
         speak("Something went wrong while searching Wikipedia.")
      else:
         output=aiprocess(c)
         speak(output)


if __name__=="__main__":
    speak("Initializing alexa.....")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")    
        try:
           with sr.Microphone() as source:
              print("Listening....")
              audio_text = r.listen(source,timeout=2,phrase_time_limit=2)
              word=r.recognize_google(audio_text)
              if (word.lower()=="alexa"):
                 speak("yes")
                 with sr.Microphone() as source:
                    print("alexa activated....")
                    audio_text = r.listen(source) 
                    command=r.recognize_google(audio_text) 
                 processcommand(command)
        except:
           speak(" babe speak")
          
