
import os
from flask import Flask, render_template, request, jsonify
from load_pages import *

app = Flask(__name__)

inverted_index = hashmap()

@app.route("/")
def home():	
	return render_template('index.html')

@app.route("/search", methods=["POST"])        
def search():
#	global inverted_index

	data = request.json
	words =  data["words"]

	response = search_query(words, inverted_index)
    #os.system('bash java.sh '+words)
	#print (response)
	return jsonify(response)

if __name__ == '__main__':
    app.run(debug = True, port=5000)
