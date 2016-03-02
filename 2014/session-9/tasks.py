import os
import Image
import requests
from celery import Celery
from StringIO import StringIO

app = Celery('tasks', broker='redis://localhost:6379/0')
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, "tasks", "thumbnails")

@app.task
def url_check(url):
	response = requests.head(url)
	result = {}
	if(response.status_code >= 300 and response.status_code <= 399):
		result['redirects'] = True
		result['redirect_url'] = response.headers.get('location', '')
		return result

	result['redirects'] = False
	return result

@app.task
def generate_thumbnail(url, file_name_to_save):
	response = requests.get(url)

	if(response.status_code == 200):
		original = Image.open(StringIO(response.content))
		original.thumbnail((100, 100), Image.ANTIALIAS)
		original.save(os.path.join(IMG_DIR, file_name_to_save), "JPEG")


