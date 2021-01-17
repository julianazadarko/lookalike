from flask import Flask, request
import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def wrapper():
    return main.run(request)