
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#dir = os.path.dirname(os.path.realpath(__file__))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search", methods=["POST"])        
def search():
    data = request.json
    words =  data["words"]

    os.system('bash java.sh '+words)
    return jsonify(words)

if __name__ == '__main__':
    app.run(debug = True, port=5000)