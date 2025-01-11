from flask import Flask, render_template
from flask_wtf import FlaskForm  
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email, ValidationError 
import bcrypt
from flask_mysqldb import MySQL


app = Flask(__name__, template_folder='templates')

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydatabase'
app.secret_key = 'your_secret_key_here'

class RegisterForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(), Email()])
    password = StringField("Password",validators=[DataRequired()])
    submit = SubmitField("Register")
       

@app.route('/')
def Hello():
    return render_template('index.html')

@app.route('/register')
def register1():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
    
    # database(store in to data base)    
        
    return render_template('register.html')

@app.route('/login')
def login1():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard1(): 
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)