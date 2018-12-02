import sys, os
sys.path.append(os.getcwd() + "/APIs")

from flask import Flask, request
from flask import render_template
from flask_pymongo import PyMongo
from Twilio import *
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

# mlab database connection
app.config['MONGO_DBNAME'] = 'website'
app.config['MONGO_URI'] = 'mongodb://nkhachan:something65@ds056419.mlab.com:56419/website'
mongo = PyMongo(app)
user = mongo.db.users

@app.route('/')
def index():
   return render_template('index.html')


@app.route("/login", methods=['GET'])
def showlogin():
   form = LoginForm()
   return render_template('login.html', title="Login", form=form)


@app.route("/login", methods=['POST'])
def login():
   form = LoginForm()

   username = request.form['username']
   password = request.form['password']
   query    = user.find({"$and":[ {"username":username}, {"password":password}]})
   id       = query[0]['_id']

   if (query.count() == 1):
      sendSMS("You logged in from " + request.remote_addr, query[0]['phone'])
      return render_template('homepage.html', title="LoggedIn", form=form, username=username, id=id)

   print("Yeah it fucked")
   return render_template('login.html', title="Login", form=form)


@app.route("/forgot", methods=['GET'])
def show_forgot():
   form = ForgotForm()
   return render_template('forgot.html', title="Forgot", form=form)


@app.route("/forgot", methods=['POST'])
def forgot():
   form  = ForgotForm()
   email = request.form['email']

   return render_template('forgot.html', title="Forgot", form=form)


@app.route("/register", methods=['GET'])
def show_register():
   form = RegisterForm()
   return render_template('register.html', title="Register", form=form)


@app.route("/register", methods=['POST'])
def register():
   form = RegisterForm()

   username   = request.form['username']
   password   = request.form['password']
   email      = request.form['email']
   phone      = request.form['phone']

   user.insert({'username': username, 'password': password, 'email': email, 'phone': phone})

   return render_template('login.html', title="Register", form=LoginForm())


#if __name__ == "__main__":
   #app.run(host="0.0.0.0", port=80)