import os
import re
import urllib
from BeautifulSoup import BeautifulSoup

BASE_DIR = "rss"

urls = {"mumbai": "http://timesofindia.feedsportal.com/c/33039/f/533975/index.rss", 
        "science": "http://timesofindia.feedsportal.com/c/33039/f/533922/index.rss",
        "business": "http://timesofindia.feedsportal.com/c/33039/f/533919/index.rss",
        "cricket": "http://timesofindia.feedsportal.com/c/33039/f/533920/index.rss"}

def init():
	if not os.path.exists(BASE_DIR):
		os.mkdir(BASE_DIR)

def clean_html(text):
	return re.sub('<[^<]+?>', '', text)

def fetch_rss(url, filename):
	file_to_save = open(os.path.join(BASE_DIR, filename), "w")

	#This method is used to connect to site and download data
	page = urllib.urlopen(url)

	#Read contents of RSS
	file_to_save.write(page.read())
	file_to_save.close()

def parse_file(filename):
	xml = open(filename).read()
	soup = BeautifulSoup(xml)
	for item in soup.findAll("item"):
		print item.title.text
		print item.pubDate
		print ""

if __name__ == "__main__":
	init()
	for filename, url in urls.items():
		print "Fetching RSS for:%s" % url
		fetch_rss(url, filename)
		parse_file(os.path.join(BASE_DIR, filename))
		print "Done fetching"
