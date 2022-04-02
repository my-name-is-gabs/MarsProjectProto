import pywhatkit as kit

def playOnYoutube(text):
    play = text.replace('youtube', '')
    kit.playonyt(play)