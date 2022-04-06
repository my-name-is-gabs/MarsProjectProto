from operator import index
import sys
from threading import Thread
import marsRecognition as mr
from marsmodules.marsWebUtil import getGlobalNews, getShowbizNews, playOnYoutube, searchInfo, getLocalNews
from marsmodules.word_dictionaries import dateTimeDictionary, closeAppDictionary, newsRequest
from marsmodules.marsDateTimeUtil import *
from marsmodules.marsUtil import getEnDefinition


running = True

mr.speak("Hi! My name is Mars, how may I help you?")

while running:

    output = mr.voice_to_text()
    print(f"You said: {output}")

    if 'mars' in output or 'maritess' in output:
        output = output.replace('mars ', '').strip() if 'mars' in output else output.replace('maritess ', '').strip()
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

        if 'ano yung' in output:
            lookfor = output.replace('ano yung ', '')
            result = searchInfo(lookfor)
            mr.speak(result)
            continue

        if 'what is' in output:
            lookfor = output.replace('what is ', '')
            result = searchInfo(lookfor)
            mr.speak(result)
            continue

        if output in newsRequest['local']:
            news = getLocalNews()
            mr.speak(news)
            continue

        if output in newsRequest['global']:
            news = getGlobalNews()
            mr.speak(news)
            continue

        if output in newsRequest['showbiz']:
            news = getShowbizNews()
            mr.speak(news)
            continue

        if 'meaning ng' in output:
            index = output.find('meaning ng ')
            word = output[index + len('meaning ng '):]
            result = getEnDefinition(word)
            mr.speak(result)
            continue


        if output in closeAppDictionary: 
            mr.speak('ByeBye!')
            break

    if output in closeAppDictionary: 
        mr.speak('ByeBye!')
        break
        
    else:
        if output == '': pass

        else:
            mr.speak('Are you saying something?')       
            continue

sys.exit('Closing the app')