import pywhatkit as kit
import wikipedia as wiki


def playOnYoutube(text):
    play = text.replace('youtube', '')
    kit.playonyt(play)


def searchInfo(text):
    try:
        return wiki.summary(text)[0:400]
    except:
        return 'Error finding answer. Try again!'


