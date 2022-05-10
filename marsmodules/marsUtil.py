from googletrans import Translator
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import random
# from word_dictionaries import writingTips

"""
This method web scraped the merriam-webster website. Web scraping is done using the bs4 module.
You can view the documentation of the bs4 here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
def getDefinition(word):
    try:
        merriam_link = requests.get(f'https://www.merriam-webster.com/dictionary/{word}').text
        soup = BeautifulSoup(merriam_link, 'html.parser')
        div = soup.find('div', class_='vg')
        span = div.find('span', class_="sb-0")
        text = span.find('span', class_="dtText").text
        
        return text

    except:
        return "Error! try again"


def marsTipsGenerator(res):
    return res[random.randint(0, len(res)-1)]
    # return res[random.randint(0, len(res)-1)]

def translateWord(word, src, dest):
    translator = Translator()

    res = translator.translate(word, dest=dest, src=src)

    return res.text

def marsWeather():
    session = HTMLSession()
    result = session.get('https://weather.com/en-PH/weather/today/l/9649a410203fa0d4c1082bc29eb8ab42e886f153fc186ac35b3e440253c85fea')

    degrees = result.html.find('span.CurrentConditions--tempValue--3a50n', first=True).text
    condition = result.html.find('div.CurrentConditions--phraseValue--2Z18W', first=True).text
    
    return f'The temperature is {degrees} and the weather condition is {condition}'

    

if __name__ == "__main__":
    marsWeather()
    translateWord('stupid', 'en', 'tl')
    # marsTipsGenerator(writingTips['response'])


