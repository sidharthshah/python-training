import random
from flask import Flask

file_to_read = open("fortune.txt")
quotes = []
app = Flask(__name__)

for line in file_to_read.readlines():
	line = line.strip()
	quotes.append(line)

@app.route("/")
def hello():
	global quotes
	num = random.randint(0, len(quotes))
	return quotes[num]

if __name__ == "__main__":
    app.run()
