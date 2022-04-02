import sys
import speech_recognition as sr
import pyttsx3 as pt

class MarsRecognition:
    
    __speech = sr.Recognizer()
    __engine = pt.init()

    def __init__(self):
        voices = self.__engine.getProperty('voices')
        self.__engine.setProperty('voice', voices[1].id)
        self.__engine.setProperty('rate', 145)
        self.__engine.setProperty('volume', 1.0)        


    def voice_to_text(self):
        command = ""
        
        with sr.Microphone() as source:
            self.__speech.adjust_for_ambient_noise(source)

            try:
                voice = self.__speech.listen(source)
                command = self.__speech.recognize_google(voice, language='en-PH')
            
            except: pass

        return command.lower()


    def speak(self, text):
        try:
            self.__engine.say(text)
            self.__engine.runAndWait()
        except: sys.exit()


# speech = sr.Recognizer()
# engine = pt.init()

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 145)
# engine.setProperty('volume', 1.0)

# def voice_to_text():
#     command = ""
    
#     with sr.Microphone() as source:
#         speech.adjust_for_ambient_noise(source)

#         try:
#             voice = speech.listen(source)
#             command = speech.recognize_google(voice, language='en-PH')
        
#         except: pass

#     return command.lower()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
        