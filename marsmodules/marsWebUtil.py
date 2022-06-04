"""
This module is a collection of mars web utilities
"""

from time import sleep
import pywhatkit as kit
import wikipedia as wiki
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

"""
This function contains the pywhatkit which has a method of playonyt that automatically redirects and play the provided string in the function.

To learn more about the pywhatkit visit here: https://pypi.org/project/pywhatkit/
"""
def playOnYoutube():
    kit.playonyt('lofi music')


def searchInfo(text):
    try:
        print(text)
        summary = wiki.summary(text, sentences=2)
        return summary
    except:
        return 'Error finding answer. Try again!'


"""
This is a function that web srapes using the bs4 module.
You can view the documentation of the bs4 here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
def getLocalNews():
    """
    This method web scrape from the website cnnphilippines that contains local news healines and return a formated string

    return <string>
    """
    local_news_html = requests.get('https://www.cnnphilippines.com/news/').text
    soup = BeautifulSoup(local_news_html, 'html.parser')

    news_article = soup.find('div', class_="col-sm-4")

    headline = news_article.find('a').text

    article_div = news_article.find('div', class_="slider-text")

    article = article_div.find('p').text

    return f"Headline: {headline}; {article}"


def getGlobalNews():
    """
    This method is also web scraped in cnnphllipines a return a formated string containing the data

    return <string>
    """
    global_news_html = requests.get('https://www.cnnphilippines.com/world/').text
    soup = BeautifulSoup(global_news_html, 'html.parser')

    news_article = soup.find('div', class_="col-sm-4")

    headline = news_article.find('a').text

    article_div = news_article.find('div', class_="slider-text")

    article = article_div.find('p').text

    return f"Headline: {headline}; {article}"


# def getShowbizNews():
#     showbiz_html = requests.get('https://www.cnnphilippines.com/entertainment/').text
#     soup = BeautifulSoup(showbiz_html, 'html.parser')

#     news_article = soup.find('div', class_="col-sm-4")

#     headline = news_article.find('a').text

#     article_div = news_article.find('div', class_="slider-text")

#     article = article_div.find('p').text

#     return f"{headline}; {article}"

def getShowbizNews():
    pep_session = HTMLSession()
    # result = session.get('https://www.pep.ph/news/local?ref=nav_v2')
    session_response = pep_session.get('https://mb.com.ph/category/entertainment/celebrities/')
    
    title = session_response.html.find('h4.title', first=True).text

    body = session_response.html.find('div.desc', first=True).text


    return f'{title}. {body}'


    

"""
This code below is used to test these functions created above.
inside the if statement, the code will only be executed when the module itself is run.
Otherwise will not execute
"""
if __name__ == "__main__":
    print("Hello world")
    print(getShobizNews())
