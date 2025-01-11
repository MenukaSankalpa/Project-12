from flask import Flask, render_template, redirect, url_for, session, flash 
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


mysql = MySQL(app)

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Register") 
    

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")         


@app.route('/')
def Hello():
    return render_template('index.html')

@app.route('/register',methods=['GET', 'POST']) 
def register1():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
    
    # database(store in to data base)  
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)", (name,email,hashed_password))
        mysql.connection.commit()
        cursor.close()
    
        return redirect(url_for('login1'))
        
    return render_template('register.html',form=form )


@app.route('/login')
def login1():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
    
    # database(store in to data base)  
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s", (email))
        user = cursor.fetchone() 
        cursor.close()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['user_id'] = user[0]
            return redirect(url_for('dashboard1')) 
        else:
            flash("Login Failed.Please check your password and username")
            return redirect(url_for('login1'))
    
    return render_template('login1.html', form=form)

@app.route('/dashboard')
def dashboard1(): 
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)