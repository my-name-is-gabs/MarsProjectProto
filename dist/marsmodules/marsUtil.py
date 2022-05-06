import requests
from bs4 import BeautifulSoup

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




