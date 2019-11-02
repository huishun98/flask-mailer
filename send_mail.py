from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config.from_object(__name__)

# DEBUG = True
# MAIL_SERVER = 'smtp.gmail.com'
# MAIL_PORT = 465,
# MAIL_USE_SSL=True

from os import getenv

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = getenv('MAIL_USERNAME', None)


# SECRET_KEY = getenv('SECRET_KEY', None)

# app.config.update(
#     DEBUG=True,
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_PORT=465,
#     MAIL_USE_SSL=True,
#     MAIL_USERNAME=app.config.from,
#     MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD'),
# )

# mail = Mail(app)

@app.route('/')
def index():
    print('hello')
    print(SECRET_KEY)

    # msg = Message('Hello',
    # sender='huishun98@gmail.com',
    # recipients=['huishun98@gmail.com'])
    # msg.body='huehue'
    # mail.send(msg)
    return 'Message sent!'

if __name__ == '__main__':
    app.run(debug=True)
