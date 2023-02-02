from flask import Flask,render_template,request,redirect,url_for,session
from flask_migrate import Migrate
from models import db,User
from dotenv import load_dotenv
load_dotenv()
import os
import re

app = Flask(__name__)
app.secret_key=os.environ["SECRET_KEY"]
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
  db.init_app(app)
  db.create_all()

migrate = Migrate(app,db)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/user')
def user():
  return render_template('user.html')

@app.route('/register',methods=['GET','POST'])
def register():
  message = ''
  if request.method == "POST":
    username = request.form['name'].strip()
    password = request.form['password'].strip()
    email = request.form['email'].strip()
    print(username,email,password,'.........................................')
    account = User.query.filter_by(email=email).first()
    all_user = User.query.all()
    if account != None:
      message='Acoount already exists !'
    elif not username or not password or not email:
      message = 'Please, fill out the form !'
    elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
      message = 'Invalid email address !'
    else:
      if len(username) != 0 and len(password) != 0 and len(email) != 0:
        user_data = User(username=username,email=email,password=password)
        db.session.add(user_data)
        db.session.commit()
        user = User.query.filter_by(email=email).first()
        message = 'You have successfully registered !'
        session['loggedin'] = True
        session['userid'] = user.id
        session['username'] = user.username
        session['email'] = user.email
        return render_template('user.html',message=message)
      else:
        message = 'fill out with proper data !'
    print(account,'>>>>>>>>>>>>>>',all_user)
    # print(all_user,'>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    
  return render_template('register.html',message=message)

@app.route('/login',methods=['GET','POST'])
def login():
  message = ''
  if request.method == "POST":
    password = request.form['password'].strip()
    email = request.form['email'].strip()
    user = User.query.filter_by(email=email).first()
    all_user = User.query.all()
    print(user,'...................',type(user))
    if user != None:
      session['loggedin'] = True
      session['userid'] = user.id
      session['username'] = user.username
      session['email'] = user.email
      message = 'Logged in successfully !'
      return render_template('user.html',message=message)
    else:
      message = 'Please enter correct email / password !'
  return render_template('login.html',message=message)

@app.route('/logout')
def logout():
  session.pop('loggedin',None)
  session.pop('userid',None)
  session.pop('email',None)
  return redirect(url_for('login'))
