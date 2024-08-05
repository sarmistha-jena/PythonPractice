# Using the requests and BeautifulSoup Python libraries, print to the screen the full text 
# of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that
#  you can read the full article without having to click any buttons.

# (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)

# This will just print the full text of the article to the screen. It will not make it easy to read, 
# so next exercise we will learn how to write this text to a .txt file.
import requests
from bs4 import BeautifulSoup
#from django.conf.urls import url

def print_article_text(base_url):
    """
    :param base_url: URL of article to scrape
    :return: naked content to text file
    """
    url_text = requests.get(base_url)
    soup = BeautifulSoup(url_text.text, 'html.parser')
    with open('article.txt', 'w') as open_file:
        for paragraph in soup.find_all(dir="ltr"):
            open_file.write(paragraph.text.replace("<span>", ""))

if __name__ == '__main__':
    url1 = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/"
    print_article_text(url1)
    print('Article text saved to article.txt')