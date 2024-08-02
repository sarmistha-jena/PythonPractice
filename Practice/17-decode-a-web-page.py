#Use the BeautifulSoup and requests Python packages to print out a list of all the 
# article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
titles = soup.findAll('h2')

for title in titles:
    print(title.text.strip())

print(len(titles))