import requests
from bs4 import BeautifulSoup
import json
import re

#--------------------------------------------------

data = {'posts':[]}

#--------------------------------------------------

def create_soup(url):
    response = requests.get(url, headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',})
    return BeautifulSoup(response.text, "html.parser")

def scrape(soup):
    posts = soup.find_all('div','box')
    for p in posts:
        p_time = p.find_all('div','post-header-datum')
        p_user = p.find_all('a','forum-user')
        p_data = p.find_all('div','forum-post-data')
        if p_user: 
            print(p_user[0].text + '  -  ' + p_time[0].text.strip())
            data['posts'].append ({
                'user': p_user[0].text,
                'time': p_time[0].text.strip(),
                'content': re.sub(r'(?:(?!\n)\s){2,}',' ',p_data[0].text.replace('\u2013','-').replace('\u00fc','ue')).split("\n")
            })

def transform_to_json():
    with open('forumposts.json','w') as output_file:
        json.dump(data, output_file, indent=4, separators=(',', ': '))

def go_to_next_page(soup):
    next_page = soup.find_all('li','naechste-seite')
    if next_page and next_page[0].a:
        url = 'https://www.transfermarkt.de' + next_page[0].a['href']
        soup = create_soup(url)
        scrape(soup)
        go_to_next_page(soup)

#--------------------------------------------------

url = input('Tippabgabe-Thread (URL): ')

soup = create_soup(url)
scrape(soup)
go_to_next_page(soup)
transform_to_json()