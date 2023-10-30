from flask import Flask, url_for

app = Flask(__name__)

@app.route("/") #http://127.0.0.1:5000
def index():
    tes ='chika'
    return f'''
    <a href="{url_for('home', myhome='this is my home')}"> Siska Aulia Utami </a>
    '''

@app.route("/home") #http://127.0.0.1:5000/home
def home():
    return "<h1>This is my home !</h1>"

@app.route('/user/<username>')
def user(username):
    # show the user profile for that user
    return f'My name is {username}'

# with app.test_request_context():
#     print(url_for('home', myhome='chika'))
