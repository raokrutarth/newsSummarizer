

from gtts import gTTS
import os
import feedparser
from bs4 import BeautifulSoup
from urllib.request import urlopen
import dateparser
import datetime

def get_rss(url):
	NewsFeed = feedparser.parse(url)
	entries = NewsFeed.entries
	print('got %d entries' % len(entries) )
	res = 'And now, updates from MIT The Download\n'
	for entry in entries:
		res += entry['title']
		res += '\n'
		try:
			res += entry['summary_detail']['value']
		except:
			pass
		res += '\n'
	return res


def get_fortune():
	urls = [
	'http://fortune.com/newsletter/ceo-daily/',
	'http://fortune.com/newsletter/datasheet/']

	t = datetime.datetime.now().strftime('%I %M %p')
	res = 'Good Morning. It is {}. News from Fortune CEO today: \n'.format(t)
	for url in urls:
		page = urlopen(url)
		soup = BeautifulSoup(page.read(), "html.parser")
		posts = soup.select('p')
		for post in posts:
			res += post.text + '\n'
	return res
