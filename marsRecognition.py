import speech_recognition as sr
import pyttsx3 as pt


# Initializing the speech recognizion and pytexttospeech module
speech = sr.Recognizer()
engine = pt.init()

# configuring the voice and its properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)
engine.setProperty('volume', 1.0)

# This is the function for listening from user's voice and converting it to a string data
def voice_to_text():
    command = ""
    
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)

        try:
            voice = speech.listen(source)
            command = speech.recognize_google(voice, language='en-PH')
        
        except: pass

    return command.lower()

# This is a simple function to make the Mars application respond using female voice
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        pass


"""
This is the commented MarsRecognition class
"""
# class MarsRecognition:
    
#     __speech = sr.Recognizer()
#     __engine = pt.init()

#     def __init__(self):
#         voices = self.__engine.getProperty('voices')
#         self.__engine.setProperty('voice', voices[1].id)
#         self.__engine.setProperty('rate', 130)
#         self.__engine.setProperty('volume', 1.0)        


#     def voice_to_text(self):
#         command = ""
        
#         with sr.Microphone() as source:
#             self.__speech.adjust_for_ambient_noise(source)

#             try:
#                 voice = self.__speech.listen(source)
#                 command = self.__speech.recognize_google(voice, language='en-PH')
            
#             except: pass

#         return command.lower()


#     def speak(self, text):
#         try:
#             self.__engine.say(text)
#             self.__engine.runAndWait()
#         except: sys.exit()
        