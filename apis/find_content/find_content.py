from googlesearch import search 

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
    return "success"
    