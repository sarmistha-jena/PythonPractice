# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want 
# to play with some different code, use the code from the solution), and instead of printing 
# the results to a screen, write the results to a txt file. In your code, just make up a name for 
# the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.

def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

import requests
from bs4 import BeautifulSoup
#from django.conf.urls import url

def save_article_file(base_url, file_name):
    """
    :param base_url: URL of article to scrape
    :return: naked content to text file
    """
    url_text = requests.get(base_url)
    soup = BeautifulSoup(url_text.text, 'html.parser')
    for paragraph in soup.find_all(dir="ltr"):
        save_to_file(paragraph.text.replace("<span>", ""), file_name)

if __name__ == '__main__':
    url1 = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/"
    file_name = input("Enter the name of the output file: ")
    save_article_file(url1, file_name)
    print('Article text saved to {}'.format(file_name))