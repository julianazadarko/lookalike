import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

#import urllib.request
#import base64


def run(request):
    request_json = request.get_json()
    email = ""
    if request.args and 'email' in request.args:
        email = request.args.get('email')
    elif request_json and 'email' in request_json:
        email = request_json['email']
    else:
        return "Requires args", 400
    
    if request.method == 'POST':
        print("test")
        return send_email(email), 200
    else:
        return "Requires post", 401

def send_email(email):
    url = "https://images.unsplash.com/reserve/Af0sF2OS5S5gatqrKzVP_Silhoutte.jpg?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cGljfGVufDB8fDB8&ixlib=rb-1.2.1&w=1000&q=80"
    #urllib.request.urlretrieve(url, "my_test.jpg")
 
    #image = 'my_test.jpg'

    #photo_string = ""
    #with open(image, "rb") as image_file:
    #    photo_string = base64.b64encode(image_file.read())
    #    photo_string = photo_string.decode()

    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("htn.lookalike@gmail.com")  # Change to your verified sender
    to_email = To(email)  # Change to your recipient
    subject = "Sending with SendGrid is Fun"
    image_str = "data:image/jpeg;base64,{}".format(photo_string)
    print(image_str)
    content= "<html><body><img src=\""+url+"\"></body></html>"
    #content = "<html><body><img src=\""+image_str+"\">test</body></html>"
    #content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, to_email, subject, html_content=content)

    
    #mail.EmbedImage("my_test.jpg","test")

    mail_json = mail.get()
    response = sg.client.mail.send.post(request_body=mail_json)
    return "test"
    """
    message = Mail(
        from_email=('htn.lookalike@gmail.com', 'LOOKALIKE'),
        to_emails=(email, "test"),
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    print(os.environ.get('SENDGRID_API_KEY'))
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    try:
        response = sg.send(message)
        print(response.status_code, response.body, response.headers)
    except Exception as e:
        print(e.message)
    """

    """
    message = Mail(
        from_email='htn.lookalike@gmail.com',
        to_emails='to@example.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
    """