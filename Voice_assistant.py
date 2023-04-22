# donwload Image
# send Mail
# Translator ->  done
# up down left right movement 
# Choose according To choice
# listening with execution
# call contacts


import pyttsx3
import speech_recognition as sr
import smtplib
import ssl
# import playsound
# import pyjokes
import wikipedia
import smtplib
import webbrowser
import ecapture as ec
import pywhatkit
import pyautogui
import twilio
# from rembg import remove
from PIL import Image
from translate import Translator

# Output from the Vc Assitant
def speak(text):
    #initialisation
    Vc_assitant = pyttsx3.init('sapi5')
    Vc_assitant.say(text)
    Vc_assitant.runAndWait()

# Input from the User
def taking_input():
    # Recognizer
    inpt = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        inpt.pause_threshold = 1
        userInpt = inpt.listen(source, timeout= 3, phrase_time_limit= 5)

    try:
        print("Recognizing The Command")
        sp2comment = inpt.recognize_google(userInpt, language= 'en-in')
        print(f"Searching on Your Input: {sp2comment}\n")
        return sp2comment
    
    except Exception as e:
        print(e)
        print("Unable to Recognize the Voice\n")
        speak("Unable to Recognize the Voice, Please Try Again Later")
        return taking_input()


# Searching From The Wikipedia
def wiki(text):
    results = wikipedia.summary(text, sentences = 2, auto_suggest = False)
    print("According to Wikipedia")
    speak("According to Wikipedia")
    print(results)
    speak(results)
    try:
        speak("Do you want to Translate it")
        your_input = taking_input()
        if your_input == 'yes' or your_input == 'Yes':
            speak("In which Language")
            your_input = taking_input()
            translator = Translator(to_lang = your_input)
            translation = translator.translate(results)
            print(translation)
            speak(translation)
    except Exception as e:
        print(e)

# Play Youtube Video
def youTube(text):
    speak("Do you want to play or search:")
    your_input = taking_input()
    if your_input == "play":
        try:
            speak("Playing on Youtube")
            pywhatkit.playonyt(text)
        
        except Exception as e:
            print(e)
    else:
        try:
            speak("Playing on Youtube")
            pywhatkit.usearch(text)
        except Exception as e:
            print(e)

# Call The Contacts
# def calling_feature():
#     try:
        


# Capture Images
def captureImage():
    speak("Capturing Image")
    ec.capture(0, "Camera", "img.jpg")

# Opening Google 
def openGoogle():
    speak("Opening Google")
    webbrowser.open("www.google.com")

# Searching Subjects in Google
def searchGoogle(text):
    try:
        speak("Searching on Google")
        pywhatkit.search(text)
    except Exception as e:
        print(e)
        print("Network Error")

# Shut Down System
def shutup(time):
    try:
        pywhatkit.shutdown(time)
    except Exception as e:
        print(e)

# Sending Emails
def mail2someone(sender_email, receiver_email, password,message):
    smtp_server = "smtp.gmail.com"
    port = 587 

    context = ssl.create_default_context()

    try:
        speak("Sending Mail in Process")
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(e)
    finally:
        server.quit() 

# Main Function
def main():
    text = "yes"
    while(text == "Yes" or text == "yes"):
        try:
            speak("Please Tell Your Request") 
            your_input = taking_input()
            your_input = your_input.lower()

            if your_input == "take photo" or your_input == "take picture":
                captureImage()

            elif your_input == "fullscreen":
                pyautogui.hotkey('f11')

            elif your_input == "open youtube":
                speak("Now what To search on youtube")
                your_input = taking_input()
                youTube(your_input)
                speak("Do you want to play the video in Full Screen")
                your_input = taking_input()
                if your_input == "yes":
                    text = 'f' or 'F'
                    pyautogui.hotkey(text)


            elif your_input == "open google":
                print("Do you want to Search on Google?")
                speak("Do you want to Search on Google?")
                your_input == taking_input().lower()
                if your_input == "yes" or "Yes":
                    speak("Now what To search on Google")
                    your_input = taking_input()
                    searchGoogle(your_input)
                else:
                    openGoogle()


            elif your_input == "send mail":
                speak("Got The Sender Details")
                sender = 'checkappsandserivices@gmail.com'
                speak("Got The Password")
                password = 'oszbhhcooymwtkrc'
                speak("Enter The Receiver Details")
                print("Enter The Receiver Details: ")
                receiver = input()
                speak("Tell The Message")
                message = taking_input()
                mail2someone(sender, receiver, password, message)

            elif your_input == "shutdown system":
                speak("Mention the Specific time after which the System will shut down")
                your_input = taking_input()
                your_input = int(your_input)
                shutup(your_input)



            elif your_input != "None":
                wiki(your_input)


            else:
                print("Run Again")
                speak("Run again")
            
            speak("Do you want need something More:")
            text = taking_input()

        except Exception as e:
            print(e)

if __name__ == "__main__":
        main()