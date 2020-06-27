from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://HomeAuto:Popat#Panda#1234$@3.6.235.34/HomeAutomation'
db=SQLAlchemy(app)

class Appliances(db.Model):
	__tablename__='appliances'
	appliance_id=db.Column('id', db.Integer , primary_key=True)
	appliance_name=db.Column('name',db.String)
	appliance_state=db.Column('state',db.Integer)
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

@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
