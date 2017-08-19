from pymongo import MongoClient
import urllib.request
from bs4 import BeautifulSoup


class Storage:
    def __init__(self):
        client = MongoClient()
        self.db = client.test5


urls = ["https://lenta.ru"]

for url in urls:
    links = {url}
    data = urllib.request.urlopen(url)
    html = data.read()
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.title.string
    for a in soup.find_all('a', href=True):
        href = a['href']
        if not href.startswith('http'):
            href = url + href
        links.add(href)
    print(links)

    storage = Storage()
    result = storage.db.restaurants6.insert_one(
        {"html": html,
         "url": url,
         "title": title})


