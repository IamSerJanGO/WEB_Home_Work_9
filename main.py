import requests
from bs4 import BeautifulSoup
import json

def scrape_quotes():
    base_url = "http://quotes.toscrape.com"
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tag = quote.find('div', class_='tags').get_text()
        quotes.append({'text': text, 'author': author, 'tags': tag})

    with open('quotes.json', 'w') as f:
        json.dump(quotes, f)

def scrape_authors():
    base_url = "http://quotes.toscrape.com"
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    authors = []
    for author in soup.find_all('div', class_='quote'):
        author_name = author.find('small', class_='author').get_text()
        author_link = base_url + author.find('a')['href']
        authors.append({'name': author_name, 'link': author_link})

    with open('authors.json', 'w') as f:
        json.dump(authors, f)

scrape_quotes()
scrape_authors()