from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://HomeAuto:Popat#Panda#1234$@3.6.235.34/HomeAutomation'
db=SQLAlchemy(app)

class Appliances(db.Model):
	__tablename__='appliances'
	appliance_id=db.Column('id', db.Integer , primary_key=True)
	appliance_name=db.Column('name' , db.String , unique=True)
	appliance_state=db.Column('state' , db.Integer)
	#appliance_user_id=db.Column('user_id',db.Integer)

class Budget(db.Model):
	__tablename__='budget'
	budget_id=db.Column('id', db.Integer , primary_key=True)
	#budget_type=db.Column('type',db.Integer)
	budget_desc=db.Column('desc',db.String)
	#budget_payment_method=db.Column('payment_method',db.Integer)
	budget_amount=db.Column('amount',db.Float)
	budget_timestamp=db.Column('timestamp',db.timestamp);
	#budget_user=db.Column('user_id',db.Integer)

class BudgetTypes(db.Model):
	__tablename__='budget_types'
	budget_type_id=db.Column('id', db.Integer , primary_key=True)
	budget_type_name=db.Column('name',db.String,unique=True)
	#budget_type_user=db.Column('user_id',db.Integer)

class BudgetPaymentMethod(db.Model):
	__tablename__='budget_payment_method'
	budget_payment_method_id=db.Column('id', db.Integer , primary_key=True)
	budget_payment_method_name=db.Column('name',db.String,unique=True)
	#budget_payment_method_user=db.Column('user_id',db.Integer)
	

class UserTable(db.model):
    __tablename__='user'
    user_id=db.Column('user_id' , db.Integer , primary_key=True)
    user_name=db.Column('name' , db.String)
    user_password=db.Column('password' , db.String)
    user_email=db.Column('email' , db.String)

class ReminderAlarm(db.model):
    __tablename__='ReminderAlarm'
    reminder_id=db.Column('id' , db.Integer, primary_key=True)
    alert_type=db.Column('alert type' , db.Integer)
    alert_description=db.Column('description' , db.String)
    alert_frequency=db.Column('frequency' , db.Integer)
    alert_time=db.Column('time' , db.Time)
    alert_day=db.Column('day' , db.Date)

class Automation(db.model):
    __tablename__='Automation'
    automation_id=db.Column("id" , db.Integer , primary_key=True)
    # automation_parameter_id=db.Column('parameter_id')
    # parameter_value=db.Column('parameter value' , db.Integer)
    # appliance_state_value=db.Column('state value' , db.Integer)
    # appliance_state_value - Tells us about when the appliance will ON/OFF

class AutomationParameter(db.model):
    __tablename='Parameter'
    parameter_id=db.Column('id' , db.Integer , primary_key=True)
    parameter_name=db.Column('name' , db.String , unique=True)
    parameter_min=db.Column('min value' , db.Integer)
    parameter_max=db.Column('max value' , db.Integer)

@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
