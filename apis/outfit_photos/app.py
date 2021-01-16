from flask import Flask, request
import outfit_photos

app = Flask(__name__)

@app.route('/', methods=['POST'])
def wrapper():
    return outfit_photos.run(request)