from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://HomeAuto:Popat#Panda#1234$@3.6.235.34/HomeAutomation'
db=SQLAlchemy(app)

class Appliances(db.Model):
	__tablename__='appliances'
	id=db.Column('id', db.Integer , primary_key=True)
	name=db.Column('name' , db.String , unique=True)
	state=db.Column('state' , db.Integer)
	user_id=db.Column('user_id',db.Integer,db.ForeignKey(''))

class Budget(db.Model):
	__tablename__='budget'
	id=db.Column('id', db.Integer , primary_key=True)
	#type=db.Column('type',db.Integer)
	desc=db.Column('desc',db.String)
	#payment_method=db.Column('payment_method',db.Integer)
	amount=db.Column('amount',db.Float)
	timestamp=db.Column('timestamp',db.timestamp);
	#user=db.Column('user_id',db.Integer)

class BudgetTypes(db.Model):
	__tablename__='budget_types'
	id=db.Column('id', db.Integer , primary_key=True)
	name=db.Column('name',db.String,unique=True)
	#user=db.Column('user_id',db.Integer)

class BudgetPaymentMethod(db.Model):
	__tablename__='budget_payment_method'
	id=db.Column('id', db.Integer , primary_key=True)
	name=db.Column('name',db.String,unique=True)
	#user=db.Column('user_id',db.Integer)
	

class UserTable(db.model):
    __tablename__='user'
    id=db.Column('id' , db.Integer , primary_key=True)
    name=db.Column('name' , db.String)
    password=db.Column('password' , db.String)
    email=db.Column('email' , db.String)

class ReminderAlarm(db.model):
    __tablename__='ReminderAlarm'
    id=db.Column('id' , db.Integer, primary_key=True)
    type=db.Column('alert type' , db.Integer)
    description=db.Column('description' , db.String)
    frequency=db.Column('frequency' , db.Integer)
    time=db.Column('time' , db.Time)
    day=db.Column('day' , db.Date)

class Automation(db.model):
    __tablename__='Automation'
    id=db.Column("id" , db.Integer , primary_key=True)
    # parameter_id=db.Column('parameter_id')
    # parameter_value=db.Column('parameter value' , db.Integer)
    # appliance_state_value=db.Column('state value' , db.Integer)
    # appliance_state_value - Tells us about when the appliance will ON/OFF

class AutomationParameter(db.model):
    __tablename='Parameter'
    id=db.Column('id' , db.Integer , primary_key=True)
   	name=db.Column('name' , db.String , unique=True)
    min=db.Column('min value' , db.Integer)
    max=db.Column('max value' , db.Integer)
#db.create_all()
#db.drop_all()

@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
