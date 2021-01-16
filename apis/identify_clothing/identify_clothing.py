import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

def run(request):
    request_json = request.get_json()
    #request_format = request.form
    img = ""
    if request.args and 'img' in request.args:
        name = request.args.get('img')
    elif request_json and 'img' in request_format:
        name = request_json.get('img')
    else:
        return "Requires args", 400
    
    if request.method == 'GET':
        print("test")
        return identify_clothing(img), 200
    else:
        return "Requires post", 401

def identify_clothing(img):
    # Instantiates a client
    url = "https://images.unsplash.com/reserve/Af0sF2OS5S5gatqrKzVP_Silhoutte.jpg?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cGljfGVufDB8fDB8&ixlib=rb-1.2.1&w=1000&q=80"
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    #file_name = os.path.abspath('../outfit_photos/my_test.jpg')

    # Loads the image into memory
    #with io.open(file_name, 'rb') as image_file:
    #    content = image_file.read()
    image = vision.Image()
    image.source.image_uri = url

    #image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)
    return "Success"