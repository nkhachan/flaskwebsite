from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
   username   = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
   email      = EmailField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
   phone      = StringField("Phone number", validators=[DataRequired()], render_kw={"placeholder": "Phone Number"})
   password   = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
   register   = SubmitField('Register')


class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
   password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
   submit   = SubmitField('Sign In')


class ForgotForm(FlaskForm):
   email = EmailField('Email address', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
   send   = SubmitField('Send Email')