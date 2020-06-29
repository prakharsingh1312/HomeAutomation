from flask import Flask , render_template , request , session , redirect , url_for
import hashlib
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'popatpanda'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://HomeAuto:Popat#Panda#1234$@3.6.235.34/HomeAutomation'
db=SQLAlchemy(app)

# Tables

class Appliances(db.Model):
	__tablename__='appliances'
	id=db.Column('id', db.Integer , primary_key=True)
	name=db.Column('name' , db.String(100) , unique=True)
	state=db.Column('state' , db.Integer)
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
	appliances=db.relationship('Appliances', backref='owner')
	budgets=db.relationship('Budget', backref='owner')
	budget_types=db.relationship('BudgetTypes', backref='owner')
	budget_payment_methods=db.relationship('BudgetPaymentMethod', backref='owner')
	reminder=db.relationship('ReminderAlarm' , backref='owner')
	parameter=db.relationship('AutomationParameter' , backref='owner')



class ReminderAlarm(db.Model):
    __tablename__='ReminderAlarm'
    id=db.Column('id' , db.Integer, primary_key=True)
    type=db.Column('alert type' , db.Integer)
    description=db.Column('description' , db.String(100))
    frequency=db.Column('frequency' , db.Integer)
    time=db.Column('time' , db.Time)
    day=db.Column('day' , db.Date)
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
# db.create_all()
# db.drop_all()
#######################
#Functions
def signup(name,password,email):

	if(UserTable.query.filter_by(email=email).count()):
		return 0
	user=UserTable(name = name , password = password , email = email)
	db.session.add(user)
	db.session.commit()
	return 1

def crypt_password(password):
	salt='maakichoot'
	password=password+salt
	password=hashlib.md5(password.encode())
	return password.hexdigest()

def login(email , password):
	if(UserTable.query.filter_by(email=email).count()):
		user=UserTable.query.filter_by(email=email).first()
		password=crypt_password(password)
		if(user.password==password):
			session['user_id']=user.id
			session['user_name']=user.name
			return 1
	return 0
def logout():
	session.pop('user_id',None)
	session.pop('user_name',None)
	return 1

####################

#ROUTES
# Home Page
@app.route("/")
def dashboard_page():
	if 'user_id' not in session:
		return redirect(url_for('login_page'))
	return render_template('index.html')
# END of Home Page

# Login Page

@app.route("/login" , methods=['GET' , 'POST'])
def login_page():
	if 'user_id' in session:
		return redirect(url_for('dashboard_page'))
	elif request.method == 'POST':
		email=request.form['email']
		password=request.form['password']
		if login(email , password):
			return redirect(url_for('dashboard_page'))
	return render_template('login-page.html')

# END of login

# Signup Page
@app.route("/signup" , methods=['GET' , 'POST'])
def signup_page():
	if 'user_id' in session:
		return redirect(url_for('dashboard_page'))
	elif request.method == 'POST':
		name = request.form['name']
		password = request.form['password']
		email = request.form['email']
		password = crypt_password(password)
		if signup(name,password,email):
			return redirect(url_for('login_page'))
	return render_template('signup-page.html')
# END of Signup Page

#Logout Route
@app.route("/logout")
def logout_page():
	if(logout()):
		return redirect(url_for('login_page'))
	return redirect(url_for('dashboard_page'))
#END of Logout Page
