import json

def analysis():

	with open('logging.json') as f:
  	data = json.load(f)

  	for key, value in data.items():
    		if key == "full_text"
    			print key, value


analysis()

