
import os
from flask import Flask, render_template, request, jsonify
from load_pages import *

app = Flask(__name__)

inverted_index = hashmap()
ranks = hashmap_pagerank()

@app.route("/")
def home():	
	return render_template('index.html')

@app.route("/search", methods=["POST"])        
def search():
#	global inverted_index
	page_rank = {}

	data = request.json
	words =  data["words"]

	response = search_query(words, inverted_index)
	for page in response:
		page_rank[page] = ranks[page]

	ranking = {k: v for k, v in sorted(page_rank.items(), key=lambda item: item[1])}	

	response = []	

	if len(ranking)<=10:
		for page in ranking:
			response.append(page)

	else:		
		for page in list(reversed(list(ranking)))[0:10]:
			response.append(page)

	#os.system('bash java.sh '+words)
	#print (response)
	return jsonify(response)		
	

if __name__ == '__main__':
    app.run(debug = True, port=5000)
