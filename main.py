import sys
from threading import Thread
from marsRecognition import MarsRecognition
from marsmodules.marsWebUtil import playOnYoutube
from marsmodules.word_dictionaries import dateTimeDictionary, closeAppDictionary
from marsmodules.marsDateTimeUtil import *



mr = MarsRecognition()


running = True

# mr.speak("Hi! My name is Mars. How may I help you?")

while running:

    output = mr.voice_to_text()
    print(f"You said: {output}")

    if 'mars' in output:
        output = output.replace('mars ', '').strip()
        print("This is Mars you said: ", output)

        if output in dateTimeDictionary['date']:
            fulldate = getFullDate()
            mr.speak(fulldate)
            continue

        if  output in dateTimeDictionary['today']:
            dayToday = getDay()
            mr.speak(dayToday)
            continue

        if output in dateTimeDictionary['time']:
            timeToday = getTime()
            mr.speak(timeToday)
            continue

        if 'youtube' in output:
            thread1 = Thread(target=playOnYoutube, args=(output,))
            thread1.start()
            continue

    if output in closeAppDictionary: 
        mr.speak('ByeBye!')
        sys.exit('Closing the application')
        
    else:
        if output == '': pass

        else:
            mr.speak('Are you saying something?')       
            continue

   