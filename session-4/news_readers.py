import os
import urllib

BASE_DIR = "rss"

urls = {"mumbai": "http://timesofindia.feedsportal.com/c/33039/f/533975/index.rss", 
        "science": "http://timesofindia.feedsportal.com/c/33039/f/533922/index.rss",
        "business": "http://timesofindia.feedsportal.com/c/33039/f/533919/index.rss",
        "cricket": "http://timesofindia.feedsportal.com/c/33039/f/533920/index.rss"}

def init():
	if not os.path.exists(BASE_DIR):
		os.mkdir(BASE_DIR)

def fetch_rss(url, filename):
	file_to_save = open(os.path.join(BASE_DIR, filename), "w")

	#This method is used to connect to site and download data
	page = urllib.urlopen(url)

	#Read contents of RSS
	file_to_save.write(page.read())
	file_to_save.close()

if __name__ == "__main__":
	init()
	for filename, url in urls.items():
		print "Fetching RSS for:%s" % url
		fetch_rss(url, filename)
		print "Done fetching"
