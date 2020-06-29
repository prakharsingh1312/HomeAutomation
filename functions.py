# Login /Signup Functions
from app import *


def signup(name,password,email):

	if(UserTable.query.filter_by(email=email).count()):
		return 0
	user_hash = random.randint(0,1000)
	user_hash=crypt_password(user_hash)
	user=UserTable(name = name , password = password , email = email , user_hash=user_hash)
	db.session.add(user)
	db.session.commit()
	return 1

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
