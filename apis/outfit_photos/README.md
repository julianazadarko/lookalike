#Setting up a venv on Windows
virtualenv --python C:\Users\{user}\AppData\Local\Programs\Python\Python39\python.exe venv

#Installing requirements:
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\activate
pip3 install -r requirements.txt

#Running flask
set FLASK_APP=app.py 
flask run

#Remember to set api key
set SENDGRID_API_KEY={KEY}