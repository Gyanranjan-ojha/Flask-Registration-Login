import datetime
from create_db import create_database
create_database()
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(20),nullable=False, unique=True)
  password = db.Column(db.String(50),nullable=False)
  email = db.Column(db.String(50),nullable=False, unique=True)
  address = db.Column(db.String(200),nullable=True)
  created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow)
  
  def __init__(self, username, email,password):
    self.username = username
    self.email = email
    self.password = password

  def __repr__(self):
    return '<User %r>' % self.username