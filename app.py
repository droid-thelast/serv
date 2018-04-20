import random, datetime, string, hashlib, os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, RadioField, IntegerField, SubmitField
from flask_admin import BaseView, Admin
from flask_user import roles_required, UserManager, UserMixin, roles_required
from flask_bcrypt import Bcrypt
from servforms import PageContent

app = Flask(__name__)

basedata = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedata, 'service.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['USER_ENABLE_EMAIL'] = False
app.config['SECRET_KEY'] = 'asecret-text'
db = SQLAlchemy(app)


class Pages(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    pages = db.Column(db.String, nullable=False)
    page_stuff = db.relationship("PageContents", backref="pages", lazy="dynamic")


class Pagecontents(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer(), primary_key=True)
    headline = db.Column(db.String(255))
    sudhead = db.Column(db.String(255))
    tags = db.Column(db.String(255))
    content = db.Column(db.String(255))
    pages_id = db.Column(db.Integer, db.ForeignKey('pages.id'))


class Faq(db.Model):
    __tablename__ = 'faq'
    id = db.Column(db.Integer(), primary_key=True)
    topic = db.Column(db.String(255))
    content = db.Column(db.String(1000))


# Define User data-model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean()),
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address1 = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    # Relationships
    roles = db.relationship('Role', secondary='user_roles')


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


# Setup Flask-User
user_manager = UserManager(app, db, User)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/huawei')
def huawei():

    return render_template('huawei.html')


@app.route('/smarthub')
def smarthub():
    return render_template('smarthub.html')


@app.route('/corporate')
def corporate():
    return render_template('corporate.html')


@app.route('/account')
def account():
    return render_template('account.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


#@app.route('/add', methods=['POST', 'GET'])
#def add():
#    form =

if __name__ == '__main__':
    app.run(port=7100, debug=True)
