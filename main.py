from flask import Flask, request
from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_pymongo import PyMongo
from wtforms.fields.html5 import EmailField


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
   register   = SubmitField('Register')


class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
   password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
   submit   = SubmitField('Sign In')


class ForgotForm(FlaskForm):
   email = EmailField('Email address', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
   send   = SubmitField('Send Email')


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
   id    = query[0]['_id']

   if (query.count() == 1):
      return render_template('homepage.html', title="LoggedIn", form=form, username=username, id=id)

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

   user.insert({'username': username, 'password': password, 'email': email})

   return render_template('register.html', title="Register", form=form)


#if __name__ == "__main__":
   #app.run(host="0.0.0.0", port=80)