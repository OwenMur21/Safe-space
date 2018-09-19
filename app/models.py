from . import db
import random
from random import choice
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
import json
from datetime import datetime
from time import time

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    crisis = db.relationship('Crisis', backref='user', lazy='dynamic')
    commentscrisis = db.relationship('Commentcrisis', backref = 'user', lazy = 'dynamic')
    Fam = db.relationship('fam', backref = 'user', lazy = 'dynamic')
    commentsfam = db.relationship('Commentfam', backref = 'user', lazy = 'dynamic')
    health = db.relationship('Health', backref = 'user', lazy = 'dynamic')
    commentshealth = db.relationship('Commenthealth', backref = 'user', lazy = 'dynamic')
    mental = db.relationship('Mental', backref = 'user', lazy = 'dynamic')
    commentsmental = db.relationship('Commentmental', backref = 'user', lazy = 'dynamic')
    last_seen = db.relationship('DateTime', backref ='user',lazy = 'dynamic')
    notifications = db.relationship('Notification', backref='user',lazy='dynamic')
    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()
            
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def username(self):
        alphabet = string.ascii_letters + string.digits
        username = ''.join(choice(alphabet) for i in range(8))
        return username
        

    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Crisis(db.Model):
    __tablename__ = 'crisis'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_name = db.Column(db.Integer, db.ForeignKey("users.name"))
    comments = db.relationship('Commentcrisis', backref='title', lazy='dynamic')

    def save_crisis(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_crisis(cls):
        crisis = Crisis.query.all()
        return crisis

class Commentcrisis(db.Model):
    __tablename__ = 'crisiscomments'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_name = db.Column(db.Integer, db.ForeignKey("users.name"))
    crisis_id = db.Column(db.Integer, db.ForeignKey('crisis.id'))
    description = db.Column(db.String(255))

    def save_comment(self):
        """
        Function that saves the crisis comments
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Commentcrisis.query.filter_by(crisis_id=id).all()
        return comment

    def __repr__(self):
        return f'Comment: {self.content}'
class Fam(db.Model):
    __tablename__ = 'fam'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_name = db.Column(db.Integer, db.ForeignKey("users.name"))
    comments = db.relationship('Commentfam', backref='title', lazy='dynamic')

    def save_Fam(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_Fam(cls):
        fam = Fam.query.all()
        return fam

class Commentfam(db.Model):
    __tablename__ = 'famcomments'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_name = db.Column(db.Integer, db.ForeignKey("users.name"))
    fam_id = db.Column(db.Integer, db.ForeignKey('fam.id'))
    description = db.Column(db.String(255))

    def save_commentl(self):
        """
        Function that saves the fam' comments
        """
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_commentsl(self, id):
        comment = Commentfam.query.filter_by(fam_id=id).all()
        return comment

    def __repr__(self):
        return f'Comment: {self.content}'

class Health(db.Model):
    __tablename__ = 'health'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_name = db.Column(db.Integer, db.ForeignKey("users.name"))
    comments = db.relationship('Commenthealth', backref='title', lazy='dynamic')

    def save_health(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_health(cls):
        health = Health.query.all()
        return health

class Commenthealth(db.Model):
    __tablename__ = 'healthcomments'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_name = db.Column(db.Integer, db.ForeignKey("users.name"))
    health_id = db.Column(db.Integer, db.ForeignKey('Health.id'))
    description = db.Column(db.String(255))

    def save_commenthealth(self):
        """
        Function that saves the health' comments
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_commenthealth(self, id):
        comment = Commenthealth.query.filter_by(health_id=id).all()
        return comment

    def __repr__(self):
        return f'Comment: {self.content}'

class Mental(db.Model):
    __tablename__ = 'mental'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_name = db.Column(db.Integer, db.ForeignKey("users.name"))
    comments = db.relationship('Comment', backref='title', lazy='dynamic')

    def save_mental(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_mental(cls):
        mental = Mental.query.all()
        return mental
                   
class Commentmental(db.Model):
    __tablename__ = 'mentalcomments'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_name = db.Column(db.Integer, db.ForeignKey("users.name"))
    mental_id = db.Column(db.Integer, db.ForeignKey('Mental.id'))
    description = db.Column(db.String(255))

    def save_commentmental(self):
        """
        Function that saves the depression' comments
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_commentmental(self, id):
        comment = Commentmental.query.filter_by(mental_id=id).all()
        return comment

    def __repr__(self):
        return f'Comment: {self.content}' 
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.Float, index=True, default=time)
    payload_json = db.Column(db.Text)

    def get_data(self):
        return json.loads(str(self.payload_json))