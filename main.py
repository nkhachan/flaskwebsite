from flask import Flask, request
from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'

# mlab database connection
app.config['MONGO_DBNAME'] = 'website'
app.config['MONGO_URI'] = 'mongodb://nkhachan:something65@ds056419.mlab.com:56419/website'
mongo = PyMongo(app)
user = mongo.db.users


class RegisterForm(FlaskForm):
   username   = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
   email      = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "Email"})
   password   = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
   confirmpwd = PasswordField('Confirm Password', validators=[DataRequired()], render_kw={"placeholder": "Confirm Password"})
   register   = SubmitField('Register')

class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
   password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
   submit   = SubmitField('Sign In')


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
   query = user.find({"$and":[ {"username":username}, {"password":password}]})
   if (query.count() == 1):
      print()
   return render_template('login.html', title="Login", form=form)


@app.route("/register", methods=['GET'])
def show_register():
   form = RegisterForm()
   return render_template('register.html', title="Register", form=form)

@app.route("/register", methods=['POST'])
def register():
   form = RegisterForm()

   username   = request.form['username']
   password   = request.form['password']
   confirmpwd = request.form['confirmpwd']
   email      = request.form['email']

   if (confirmpwd == password):
      user.insert({'username': username, 'password': password, 'email': email})

   return render_template('register.html', title="Register", form=form)

