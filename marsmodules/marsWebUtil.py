import pywhatkit as kit
import wikipedia as wiki
import requests
from bs4 import BeautifulSoup

def playOnYoutube(text):
    play = text.replace('youtube', '')
    kit.playonyt(play)


def searchInfo(text):
    try:
        print(text)
        summary = wiki.summary(text, sentences=2)
        return summary
    except:
        return 'Error finding answer. Try again!'


def getLocalNews():
    local_news_html = requests.get('https://www.cnnphilippines.com/news/').text
    soup = BeautifulSoup(local_news_html, 'html.parser')

    news_article = soup.find('div', class_="col-sm-4")

    headline = news_article.find('a').text

    article_div = news_article.find('div', class_="slider-text")

    article = article_div.find('p').text

    return f"Headline: {headline}; {article}"


def getGlobalNews():
    global_news_html = requests.get('https://www.cnnphilippines.com/world/').text
    soup = BeautifulSoup(global_news_html, 'html.parser')

    news_article = soup.find('div', class_="col-sm-4")

    headline = news_article.find('a').text

    article_div = news_article.find('div', class_="slider-text")

    article = article_div.find('p').text

    return f"Headline: {headline}; {article}"


def getShowbizNews():
    showbiz_html = requests.get('https://www.cnnphilippines.com/entertainment/').text
    soup = BeautifulSoup(showbiz_html, 'html.parser')

    news_article = soup.find('div', class_="col-sm-4")

    headline = news_article.find('a').text

    article_div = news_article.find('div', class_="slider-text")

    article = article_div.find('p').text

    return f"{headline}; {article}"
    

if __name__ == "__main__":
    getShowbizNews()