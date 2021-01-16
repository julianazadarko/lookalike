from flask import Flask, request
import identify_clothing

app = Flask(__name__)

@app.route('/', methods=['GET'])
def wrapper():
    print('hello')
    return identify_clothing.run(request)