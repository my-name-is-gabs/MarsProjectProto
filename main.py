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
from marsmodules.word_dictionaries import *
from marsmodules.marsDateTimeUtil import *
from marsmodules.marsUtil import getDefinition, marsTipsGenerator, marsWeather, translateWord


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
        # if 'play some music' in output:
        #     # Threading is used here because the function playOnYoutube() which run from the module pywhatkit
        #     # thread1 = Thread(target=playOnYoutube, args=(output,)) this is old where it accepts an argument

        #     thread1 = Thread(target=playOnYoutube)
        #     thread1.start()
        #     continue

        # For asking question through wikipedia
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

        # For getting the definition of a vocabolary words through Merriam webster dictionary website
        if 'meaning ng' in output:
            # Here, I manipulate the string by finding the index of 'meaning ng ' and storing the value to index variable
            index = output.find('anong meaning ng ')
            # Then I will use the slice operation to select the start and the end of the string
            word = output[index + len('anong meaning ng '):]
            result = getDefinition(word)
            mr.speak(result)
            continue
        
        # For getting tips 
        if output in writingTips['prompt']:
            tip = marsTipsGenerator(writingTips['response'])
            mr.speak(tip)
            continue

        if output in focusSkillTips['prompt']:
            tip = marsTipsGenerator(focusSkillTips['response'])
            mr.speak(tip)
            continue

        # For generating weather forecast
        if output in weatherPrompt:
            weather = marsWeather()
            mr.speak(weather)
            continue

        # for translating a word from Filipino to English
        if 'anong english ng ' in output:
            index = output.find('anong english ng ')
            word = output[index + len('anong english ng '):]
            result = translateWord(word, 'tl', 'en')
            mr.speak(result)
            continue
        # for translating a word from English to Filipino
        if 'anong tagalog ng ' in output:
            index = output.find('anong tagalog ng ')
            word = output[index + len('anong tagalog ng '):]
            result = translateWord(word, 'en', 'tl')
            mr.speak(result)
            continue

        # For closing the application
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