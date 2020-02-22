# Send Mail

## Description
This is a simple Flask application that receives POST requests to send emails to specified users. The live version can be found here: http://hs-flask-mailer.herokuapp.com/.

## Running locally
1. Create a .env file consisting of the following:
    - MAIL_USERNAME
    - MAIL_PASSWORD
    - RECIPIENT_EMAIL
    - LOCAL_HOST
    - APP_HOST

2. Download the required libraries
~~~
pip install -r requirements.txt
~~~

3. Run the app
~~~ 
python wsgi.py 
~~~
