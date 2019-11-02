from flask import Flask
from flask_mail import Mail, Message
import os
from os import getenv
from dotenv import load_dotenv

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
def index():
    msg = Message('New message from Portfolio website',
                  sender='huishunchua@gmail.com',
                  recipients=[getenv('MAIL_USERNAME', None)])
    msg.body = 'huehue'
    mail.send(msg)
    return 'Message sent!'


if __name__ == '__main__':
    app.run(debug=True)
