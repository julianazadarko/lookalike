from flask import Flask, request
import main

app = Flask(__name__)

@app.route('/', methods=['POST'])
def wrapper():
    return main.run(request)