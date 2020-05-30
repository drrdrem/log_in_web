from web import db, bcrypt, app
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from datetime import datetime
from markdown import markdown
from flask import url_for
import bleach
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.utils import secure_filename
import os
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# Allowable HTML tags
allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                'h1', 'h2', 'h3', 'p']


class ValidationError(ValueError):
    """Class for handling validation errors during
       import of recipe data via API
    """
    pass


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # lastname = db.Column(db.String(64), index=True)
    # firstname = db.Column(db.String(64), index=True)
    # email_confirmation_sent_on = db.Column(db.DateTime, nullable=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # phone = db.Column(db.String(64), index=True)
    # occupation = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    # email_confirmed_on = db.Column(db.DateTime, nullable=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def is_correct_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return '<User {}>'.format(self.username)
