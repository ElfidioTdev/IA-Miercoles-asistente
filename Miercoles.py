import pyttsx3 #pip install pyttsx3 
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("La Fecha actual es")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Bienvenido Señor!")

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Buenos dias!")
    elif hour >=12 and hour < 18: 
        speak("Buenas Tardes!")
    elif hour >= 18 and hour <=24:
        speak("Buenas Noches")
    else:
        speak("Good Night!")
    speak("Soy Miercoles estoy a su servicio. Como puedo Ayudarte hoy?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recononciendo...")
        query = r.recognize_google(audio, language = 'es-ES')
        print(query)
    except Exception as e:
        print(e)
        speak("Puedes decirlo otra vez? porfavor...")
    
        return "None"
    
    return query
def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("elfidiotevez@gmil.com", "673818192994irbzjd")
    server.sendmail("text@gmail.com", to , content)
    server.close()

if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "hora" in query:
            time()
        elif "fecha" in query:
             date()
        elif"adiós" in query:
            speak("Adios Señor!")
            quit()
        elif "wikipedia" in query:
            speak("Buscando...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Deacuerdo con Wikipedia")
            print(results)
            speak(results)
        elif "enviar correo" in query:
            try:
                speak("Que quieres que diga?")
                content = takeCommand()
                to = "viserionnetzek@gmail.com"
                #sendemail(to,content)
                speak("Email enviado con exito")
                speak(content)
            except Exception as e:
                speak(e)
                speak("No se puede enviar el mensaje")
        elif "navegador" in query:
            speak("que deseas buscar?")
            search = takeCommand().lower()
            wb.open_new_tab("https://" + search + ".com")
            speak("El navegador esta abierto")

        elif 'youtube' in query:
            wb.open_new_tab("https://www.youtube.com")
            speak("youtube esta abierto ahora Señor")
            

        elif 'google' in query:
            wb.open_new_tab("https://www.google.com")
            speak("Google chrome esta abierto Señor")
            

        elif 'gmail' in query:
            wb.open_new_tab("https://www.gmail.com")
            speak("Google Mail Esta abierto señor")


        elif 'discord' in query:
            speak("Desea Abrirlo?")
            si = takeCommand().lower()
            speak("Discord se abrira pronto")

        elif 'buscador' in query:
            speak("que deseas buscar?")
            busca = takeCommand().lower()
            wb.open_new_tab("https://www.youtube.com/results?search_query=" + busca)
            speak("su busqueda sobre"+ busca + "se abrira pronto")

        elif 'mix 1' in query:
            speak("Deseas reproducir el mix1?")
            si = takeCommand().lower()
            wb.open_new_tab("https://www.youtube.com/watch?v=L_RNv6for7k&list=RDL_RNv6for7k")
            speak("Reproducire el mix 1 en Youtube")

            

        