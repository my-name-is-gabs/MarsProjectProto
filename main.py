"""
This is the Mars smart assitant application created by Group 7

Members:
Roxas, Trishia
Solomon, Danica
Silaga, Rochelle
Sombrito, Antonio
Sombrito, Maynard
Villar, Gabriel

"""
import sys
from threading import Thread
import marsRecognition as mr
from marsmodules.marsWebUtil import getGlobalNews, getShowbizNews, playOnYoutube, searchInfo, getLocalNews
from marsmodules.word_dictionaries import dateTimeDictionary, closeAppDictionary, newsRequest
from marsmodules.marsDateTimeUtil import *
from marsmodules.marsUtil import getDefinition


running = True

mr.speak("Hi! My name is Mars, how may I help you?")

while running:
    # This is where the converted voice to text data string will be stored
    output = mr.voice_to_text()
    print(f"You said: {output}")

    # In order for the application to start executing the commands, the user must say the word mars or marites as a trigger
    # The martess is spelled with double 's' because the speech recognition API returns the spelling of the name with double 's'.
    # changing the spelling might cause a bug so it is advisable to leave it as is
    if 'mars' in output or 'maritess' in output:
        output = output.replace('mars ', '').strip() if 'mars' in output else output.replace('maritess ', '').strip()
        print("This is Mars you said: ", output)

        # if the output matches string stored in the dateTimeDictionary
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

        # If 'youtube' is present from the output, then the following functions will execute
        if 'youtube' in output:
            # Threading is used here because the function playOnYoutube() which run from the module pywhatkit
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

        # The newsRequest dictionary is a collection of words to be used in order to execute the following functions.
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
            # Here, I manipulate the string by finding the index of 'meaning ng ' and storing the value to index variable
            index = output.find('meaning ng ')
            # Then I will use the slice operation to select the start and the end of the string
            word = output[index + len('meaning ng '):]
            result = getDefinition(word)
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