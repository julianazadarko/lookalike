from googlesearch import search 
from bs4 import BeautifulSoup as BSHTML
import urllib.request
#from bs4 import BeautifulSoup
#import requests

def run(request):
    request_json = request.get_json()
    #request_format = request.form
    name = ""
    if request.args and 'name' in request.args:
        name = request.args.get('name')
    elif request_json and 'name' in request_format:
        name = request_json.get('name')
    else:
        return "Requires args", 400
    
    if request.method == 'GET':
        print("test")
        return find_page(name), 200
    else:
        return "Requires post", 401

def find_page(name, context="instagram"):
    if(context == "instagram"):
        query = name + " " + context
  
    print(query)
    ig_pg = ""
    for j in search(query, tld="com", num=10, stop=10, pause=2): 
        if(j.find("instagram.com")):
            ig_pg = j
            break
        print(j) 

    print(ig_pg)


    page = urllib.request.urlopen(ig_pg)
    soup = BSHTML(page)
    images = soup.findAll('img')
    for image in images:
        #print image source
        print(image['src'])
        #print alternate text
        print(image['alt'])

    """

    res = requests.get(ig_pg)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    print(soup.prettify())
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    print(img_tags)
    print(urls)
    """

    return "success"
    