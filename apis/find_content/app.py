from flask import Flask, request
import find_content

app = Flask(__name__)

@app.route('/', methods=['GET'])
def wrapper():
    return find_content.run(request)