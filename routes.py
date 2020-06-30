
from functions import *

#ROUTES
# Home Page
@app.route("/")
def dashboard_page():
	if 'user_id' not in session:
		return redirect(url_for('login_page'))
	return render_template('index.html' , page='Dashboard')
# END of Home Page

# Login Page

@app.route("/login" , methods=['GET' , 'POST'])
def login_page():
	err=0;
	dologin = -1
	if 'login' in session:
		dologin=session['login']
		session.pop('login',None)
	elif 'user_id' in session:
		return redirect(url_for('dashboard_page'))
	elif request.method == 'POST':
		email=request.form['email']
		password=request.form['password']
		dologin = login(email , password)
		if dologin == 1:
			return redirect(url_for('dashboard_page'))
	return render_template('login-page.html',login=dologin)

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
			session['login']=3
			return redirect(url_for('.login_page'))
	return render_template('signup-page.html')
# END of Signup Page

#Logout Route
@app.route("/logout")
def logout_page():
	if(logout()):
		return redirect(url_for('login_page'))
	return redirect(url_for('dashboard_page'))
#END of Logout Page

@app.route("/automation")
def automation_page():
	if 'user_id' not in session:
		return redirect(url_for('login_page'))
	return render_template('automation.html' , page='Automation')

@app.route("/expenses")
def expenses_page():
	if 'user_id' not in session:
		return redirect(url_for('login_page'))
	return render_template('expenses.html' , page='Expenses')

@app.route("/alarms")
def alarms_page():
	if 'user_id' not in session:
		return redirect(url_for('login_page'))
	return render_template('alarms.html' , page='Alarms & Reminders')

@app.route("/appliances")
def appliances_page():
	if 'user_id' not in session:
		return redirect(url_for('login_page'))
	appliances=show_appliances()
	return render_template('appliances.html' , page='Appliances' , appliances=appliances)

@app.route("/user" , methods=['GET' , 'POST'])
def user_page():
	if 'user_id' not in session:
		return redirect(url_for('login_page'))
	elif request.method == 'POST':
		msg=None
		if request.form['submit'] == 'update_profile':
			user_name=request.form['user']
			user_email=request.form['email']
			user_password=request.form['password']
			if update_user_profile(user_name,user_email,user_password):
				msg='Profile Updated Successfully'
				flash(msg,'success')
			else:
				msg='Invalid Password'
				flash(msg,'danger')
		elif request.form['submit'] == 'update_pass':
			password=request.form['old_password'];
			new_password=request.form['new_password']
			if password_change(password,new_password):
				msg='Password Updated Successfully'
				flash(msg,'success')
			else:
				msg='Invalid Password'
				flash(msg,'danger')


	user=get_user_details()
	return render_template('User_profile.html' , page='User Profile' , user=user)

@app.route("/verify")
def verify_page():
	session['login']=5
	if 'verify' in request.args:
		token=request.args['token']
		user_hash=request.args['hash']
		if verify(token,user_hash):
			session['login']=4
	return redirect(url_for('.login_page'))

@app.route("/temp")
def temp_page():
	return render_template('2.html')
