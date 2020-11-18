
import os
from flask import Flask, render_template, request, jsonify
from load_pages import *

app = Flask(__name__)

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

	words = words.lower().split()

	response  = search_query(words)

	pagelist = []

	if not len(response):
		return jsonify([])

	else:

		for lista in response:

			for page in lista[0]:

				if page in page_rank:
					
					page_rank[page][1] += ' '+lista[1]
				else:	
					page_rank[page] = [ranks[page], lista[1]]

		#if not len(page_rank):		
		#	return jsonify([])			

		page_rank = {k: v for k, v in sorted(page_rank.items(), reverse=True, key=lambda item: item[1][0])}		

		if len(page_rank)<=10:
			for key in page_rank:
			    temp = [key,page_rank[key]]
			    pagelist.append(temp)

			return jsonify(pagelist)
				
		else:				
			temp_dic = dict(list(page_rank.items())[:10])	
			for key in temp_dic:
			    temp = [key,temp_dic[key]]
			    pagelist.append(temp)	

			return jsonify(pagelist)

	#os.system('bash java.sh '+words)
	#print (response)
	
	

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)
