# Login /Signup Functions
from app import *


def signup(name,password,email):

	if(UserTable.query.filter_by(email=email).count()):
		return 0
	user_hash = random.randint(0,1000)
	user_hash=crypt_password(user_hash)
	token=crypt_password(email)
	reciever=[]
	reciever.append(email)
	user=UserTable(name = name , password = password , email = email , user_hash=user_hash)
	subject='Login | Verification'
	message="You can login after you have verified your email address. Please click this link to verify you email address: http://3.6.235.34:5000/verify?token="+str(token)+"&hash="+str(user_hash)+"&verify"
	if send_mail(message , reciever , subject):
		db.session.add(user)
		db.session.commit()
		return 1
	return 0

def crypt_password(password):
	salt='maakichoot'
	password=str(password)+salt
	password=hashlib.md5(password.encode())
	return password.hexdigest()

def login(email , password):
	if(UserTable.query.filter_by(email=email).count()):
		user=UserTable.query.filter_by(email=email).first()
		password=crypt_password(password)
		if not user.user_activated:
			return 3
		elif user.password == password:
			session['user_id']=user.id
			session['user_name']=user.name
			return 1
		else:
			return 0
	return 2

def logout():
	session.pop('user_id',None)
	session.pop('user_name',None)
	return 1

def get_user_details():
	user_id=session['user_id']
	user=UserTable.query.filter_by(id=user_id).first()
	return user

def update_user_profile(name , email , password):
	user_id=session['user_id']
	user=UserTable.query.filter_by(id=user_id).first()
	password=crypt_password(password)
	if(user.password==password):
		session['user_name']=name
		user.name=name
		user.email=email
		db.session.commit()
		return 1
	return 0

def password_change(password , new_password):
	user=UserTable.query.filter_by(id=session['user_id']).first()
	password=crypt_password(password)
	if user.password == password:
		user.password=crypt_password(new_password)
		db.session.commit()
		return 1
	return 0

def send_mail(message , reciever , subject):
	msg = Message(subject, recipients=reciever , sender = ['Ritik' , 'prakharsingh13@gmail.com'])
	msg.body=message
	mail.send(msg)
	return 1

def verify(token, hash):
	user=UserTable.query.filter_by(user_hash=hash).first()
	user_email=crypt_password(user.email)
	if token == user_email:
		user.user_activated=1
		user.user_hash=''
		db.session.commit()
		return 4
	return 0
def show_appliances():
	user_id=session['user_id']
	appliances=Appliances.query.filter_by(user_id=user_id)
	return appliances
def add_appliance(name , state , pin_number):
	if not Appliances.query.filter_by(user_id = session['user_id'] , pin_number = pin_number).count():
		if not Appliances.query.filter_by(user_id = session['user_id'] , name = name).count():
			user=UserTable.query.filter_by(id=session['user_id']).first()
			appliance=Appliances(name=name , state=state , pin_number=pin_number , owner = user)
			db.session.add(appliance)
			db.session.commit()
			return 1
		return 2
	return 0
def toggle_appliance(appliance_id):
	appliance=Appliances.query.filter_by(user_id = session['user_id'] , id=appliance_id)
	if appliance.count():
		appliance=appliance.first()
		appliance.state=(appliance.state + 1) % 2
		db.session.commit()
		return '1'
	return '0'

def update_appliance(id , name , pin , state):
	if not Appliances.query.filter(Appliances.user_id == session['user_id'] , Appliances.pin_number == pin, Appliances.id != id).count():
		if not Appliances.query.filter(Appliances.user_id == session['user_id'] , Appliances.name == name , Appliances.id != id).count():
			appliance=Appliances.query.filter_by(id=id).first()
			appliance.name=name
			appliance.pin_number=pin
			appliance.state=state
			db.session.commit()
			return 1
		return 2
	return 0

def delete_appliance(id):
	if Appliances.query.filter_by(user_id = session['user_id'] , id=id).count():
		appliance=Appliances.query.filter_by(user_id = session['user_id'] , id=id).first()
		db.session.delete(appliance)
		db.session.commit()
		return 1
	return 0

def show_alarms():
	user_id=session['user_id']
	alarms=ReminderAlarm.query.filter_by(user_id = user_id,type=1)
	return alarms

def show_reminders():
	user_id=session['user_id']
	reminders=ReminderAlarm.query.filter_by(user_id = user_id,type=2)
	return reminders

def add_alerts(type , description , frequency , time , day , id=0):
	user_id = session['user_id']
	if not id:
		if type == 1:
			user=UserTable.query.filter_by(id = user_id).first()
			alarms=ReminderAlarm(type = type , description = description , frequency = frequency , time = time  , owner=user)
			db.session.add(alarms)
			db.session.commit()
			return 1
		elif type == 2:
			user=UserTable.query.filter_by(id = user_id).first()
			reminders=ReminderAlarm(type = type , description = description  , time = time , day = day)
			db.session.add(reminders)
			db.session.commit()
			return 2
	elif id :
			if type == 1:
				update_alarm = ReminderAlarm.query.filter_by(user_id = user_id , id=id).first()
				print(update_alarm)
				update_alarm.description = description
				update_alarm.frequency = frequency
				update_alarm.time = time
				db.session.commit()
				return 3
			elif type == 2:
				update_reminder = ReminderAlarm.query.filter_by(user_id = user_id , id=id).first()
				update_reminder.description = descripotion
				update_reminder.time = time
				update_reminder.day = day
				db.session.commit()
				return 4
	return 0

def delete_alert(id):
	if ReminderAlarm.query.filter_by(user_id = session['user_id'] , id=id).count():
		alert=ReminderAlarm.query.filter_by(user_id = session['user_id'] , id=id).first()
		db.session.delete(alert)
		db.session.commit()
		return 1
	return 0

def toggle_alert(alert_id):
	alert=ReminderAlarm.query.filter_by(user_id = session['user_id'] , id=alert_id)
	if alert.count():
		alert=alert.first()
		alert.state=(alert.state + 1) % 2
		db.session.commit()
		return '1'
	return '0'
