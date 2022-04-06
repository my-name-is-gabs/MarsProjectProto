import requests
from bs4 import BeautifulSoup


def getEnDefinition(word):
    try:
        merriam_link = requests.get(f'https://www.merriam-webster.com/dictionary/{word}').text
        soup = BeautifulSoup(merriam_link, 'html.parser')
        div = soup.find('div', class_='vg')
        span = div.find('span', class_="sb-0")
        text = span.find('span', class_="dtText").text
        
        return text

    except:
        return "Error! try again"
