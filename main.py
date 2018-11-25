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

class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   submit   = SubmitField('Sign In')

@app.route('/')
def index():
   return render_template('index.html')


@app.route("/login", methods=['GET'])
def loginshow():
   form = LoginForm()
   return render_template('login.html', title="Login", form=form)


@app.route("/login", methods=['POST'])
def login():
   form = LoginForm()
   username = request.form['username']
   password = request.form['password']
   user = mongo.db.users
   user.insert({'username': username, 'password': password})
   return render_template('login.html', title="Login", form=form)
