from flask import Flask , render_template , request , session , redirect , url_for,flash
import hashlib
from datetime import datetime
import random
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail , Message
app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'email',
    MAIL_PASSWORD = 'password'
)
mail=Mail(app)
app.secret_key = 'popatpanda'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@host/database'
db=SQLAlchemy(app)

# Tables

class Appliances(db.Model):
	__tablename__='appliances'
	id=db.Column('id', db.Integer , primary_key=True)
	name=db.Column('name' , db.String(100))
	state=db.Column('state' , db.Integer)
	pin_number=db.Column('pin_number' , db.Integer)
	user_id=db.Column('user_id',db.Integer,db.ForeignKey('user.id'))

class Budget(db.Model):
	__tablename__='budget'
	id=db.Column('id', db.Integer , primary_key=True)
	#type=db.Column('type',db.Integer)
	desc=db.Column('desc',db.String(1000))
	#payment_method=db.Column('payment_method',db.Integer)
	amount=db.Column('amount',db.Float)
	timestamp=db.Column('timestamp',db.DateTime);
	user_id=db.Column('user_id',db.Integer,db.ForeignKey('user.id'))
	budget_type_id=db.Column('budget_types_id' , db.Integer , db.ForeignKey('budget_types.id'))
	budget_payment_id=db.Column('budget_payment_method_id' , db.Integer , db.ForeignKey('budget_payment_method.id'))


class BudgetTypes(db.Model):
	__tablename__='budget_types'
	id=db.Column('id', db.Integer , primary_key=True)
	name=db.Column('name',db.String(100),unique=True)
	user_id=db.Column('user_id',db.Integer,db.ForeignKey('user.id'))

	budget_types=db.relationship('Budget' , backref='budget_type')

class BudgetPaymentMethod(db.Model):
	__tablename__='budget_payment_method'
	id=db.Column('id', db.Integer , primary_key=True)
	name=db.Column('name',db.String(100),unique=True)
	user_id=db.Column('user_id',db.Integer,db.ForeignKey('user.id'))
	payment=db.relationship('Budget' , backref='budget_meth')



class UserTable(db.Model):
	__tablename__='user'
	id=db.Column('id' , db.Integer , primary_key=True)
	name=db.Column('name' , db.String(100))
	password=db.Column('password' , db.String(100))
	email=db.Column('email' , db.String(100) , unique=True)
	user_hash=db.Column('hash' , db.String(100))
	user_activated=db.Column('activated' ,db.Integer, default=0)
	appliances=db.relationship('Appliances', backref='owner')
	budgets=db.relationship('Budget', backref='owner')
	budget_types=db.relationship('BudgetTypes', backref='owner')
	budget_payment_methods=db.relationship('BudgetPaymentMethod', backref='owner')
	reminder=db.relationship('ReminderAlarm' , backref='owner')
	parameter=db.relationship('AutomationParameter' , backref='owner')



class ReminderAlarm(db.Model):
	__tablename__='ReminderAlarm'
	id=db.Column('id' , db.Integer, primary_key=True)
	type=db.Column('alert_type' , db.Integer)
	description=db.Column('description' , db.String(100))
	frequency=db.Column('frequency' , db.Integer)
	time=db.Column('time' , db.Time)
	day=db.Column('day' , db.Date)
	state=db.Column('state' ,db.Integer ,default=1)
	user_id=db.Column('user_id' , db.Integer , db.ForeignKey('user.id'))


class Automation(db.Model):
    __tablename__='Automation'
    id=db.Column("id" , db.Integer , primary_key=True)
    parameter_id=db.Column('parameter_id' , db.Integer)
    parameter_value=db.Column('parameter value' , db.Integer)
    appliance_state_value=db.Column('state value' , db.Integer)
    automation_parameter_id=db.Column('Automation_paraqmeter_id' , db.Integer , db.ForeignKey('Parameter.id'))


class AutomationParameter(db.Model):
	__tablename__='Parameter'
	id=db.Column('id' , db.Integer , primary_key=True)
	name=db.Column('name' , db.String(100), unique=True)
	min=db.Column('min value' , db.Integer)
	max=db.Column('max value' , db.Integer)
	parameter=db.relationship('Automation' , backref='owner')

	user_id=db.Column('user_id' , db.Integer , db.ForeignKey('user.id'))
#db.create_all()
#db.drop_all()
#######################

####################
