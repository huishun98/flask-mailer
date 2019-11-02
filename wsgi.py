import flask
from flask import Flask, request
from flask_mail import Mail, Message
import os
from os import getenv
from dotenv import load_dotenv
from flask_cors import cross_origin
import json

app = Flask(__name__)

app.config.from_object(__name__)
load_dotenv()

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,
    MAIL_USERNAME=getenv('MAIL_USERNAME', None),
    MAIL_PASSWORD=getenv('MAIL_PASSWORD', None),
)

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
@cross_origin([getenv('LOCAL_HOST', None), getenv('APP_HOST', None)])
def index():
    if flask.request.method == 'GET':
        return 'Sorry, this service only allows POST requests.'

    jsonResponse = json.loads(request.data.decode('utf-8'))
    msg = Message('New message from Portfolio website',
                  sender=getenv('MAIL_USERNAME', None),
                  recipients=[getenv('RECIPIENT_EMAIL', None)])
    name = jsonResponse.get('name')
    email = jsonResponse.get('email')
    content = jsonResponse.get('message')
    msg.body = 'Name: {name}\r\nEmail: {email}\r\nMessage: {content}'.format(
        name=name,
        email=email,
        content=content
    )
    mail.send(msg)
    return 'Message sent!'


if __name__ == '__main__':
    app.run(debug=True)
