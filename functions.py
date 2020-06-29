# Login /Signup Functions
from app import *


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

def get_user_details():
	user_id=session['user_id']
	user=UserTable.query.filter_by(id=user_id).first()
	return user

def update_user_profile(name , email):
	user_id=session.['user_id']
	user=UserTable.query.filter_by(id=user_id).first()
	user.name=name
	user.email=email
	db.session.commit()
