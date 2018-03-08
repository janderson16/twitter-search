import requests
from bs4 import BeautifulSoup

url = u'https://twitter.com/search?q='
query= u'%40turingschool'

r = requests.get(url+query)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]

print(tweets)
