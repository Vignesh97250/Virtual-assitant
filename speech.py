import speech_recognition as sr
from gtts import gTTS
import playsound
import webbrowser

def listen():
    '''obtain audio from the microphone'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Hey Guy start talking")
        audio=r.listen(source,phrase_time_limit=5)
    data=''
    try:
        data=r.recognize_google(audio,
                              language='en-US')
        print(" You said "+data)
    except sr.UnknownValueError:
        print("I cannot hear you speak louder")
    except sr.RequestError as e:
        print("Microphone is not working")
    #return data
    tts=gTTS(data)
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
listen() 
def respond (string):
    '''function'''
    tts=gTTS(text=string)
    tts.save('speech.mp3')
    filename='speech%s.mp3'%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
def virtualasaiatant(data):
    if 'how are you' in data:
        listining=True
        respond('fine this is vignesh  u')
    elif 'time' in data:
        listining=True
        respond('weekend plan')
    elif 'you thinking' in data:
        listining=True
        respond('weekend plan')
    elif 'open google' in data.lower():
        listining=True
        url = 'https://www.google.com/'
        webbrowser.open(url)
        respond('succces')
    elif 'locate' in data:
        listining=True
        webbrowser.open('https://www.google.com/maps/search/'+
                        data.replace('locate',""))
        result='located'
        respond('Locateed {}'.formate(data.replace("locate","")))
    elif 'who are you' in data:
        listining=True
        respond('i am')
    elif 'stop talking' in data:
        listining=False
        respond('okay take care')
    try:
        return listening
    except:
        print('stopped')
    respond('Hey')
listening = True
while listening == True:
    data = listen()
    listening = virtual_assistant(data)


