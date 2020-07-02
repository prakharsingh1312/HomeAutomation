
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

@app.route("/alarms" , methods=['GET' , 'POST'])
def alarms_page():
	if 'user_id' not in session:
		return redirect(url_for('login_page'))
	elif request.method == 'POST':
		msg = None
		if request.form['submit'] == 'add_alarm':
			type=1
			description=request.form['description']
			frequency=0
			for freq in request.form.getlist('frequency'):
				frequency+=int(freq)
			time=datetime.strptime(request.form['time'],'%I:%M %p')
			day='0'
			flag = add_alerts(type , description,frequency , time , day)
			if flag == 1:
				msg='Alarm has been added successfully.'
				flash(msg,'success')
			else:
				msg='Alarm was not added.'
				flash(msg,'danger')
		elif request.values['submit'] == 'add_reminder':
			type=2
			description=request.form['description']
			frequency=0
			for freq in request.form['frequency']:
				frequency+=int(freq)
			time=datetime.strptime(request.form['time'],'%I:%M %p')
			day=request.form['day']
			flag = add_alerts(type , description , frequency , time , day)
			if flag == 2:
				msg='Reminder has been added successfully.'
				flash(msg,'success')
			else:
				msg='Cannot add Reminder.'
				flash(msg,'danger')
		elif request.values['submit'] == 'edit_alarm':
			type=1
			description=request.form['description']
			frequency=0
			day='0'
			id=request.form['id']
			for freq in request.form.getlist('frequency'):
				frequency+=int(freq)
			time=datetime.strptime(request.form['time'],'%I:%M %p')
			flag = add_alerts(type , description , frequency , time , day , id)
			if flag == 3:
				msg='Alarm has been updated successfully.'
				flash(msg,'success')
			else:
				msg='Cannot update alarm.'
				flash(msg,'danger')
		elif request.values['submit'] == 'edit_reminder':
			type=2
			description=request.form['description']
			frequency=request.form['frequency']
			time=request.form['time']
			day=request.form['day']
			flag = add_alerts(type , description , frequency , time , day , id)
			if flag == 4:
				msg='Reminder has been updated successfully.'
				flash(msg,'success')
			else:
				msg='Cannot update reminder.'
				flash(msg,'reminder')
		elif request.values['submit'] == 'toggle':
			alert_id = request.values['id']
			return toggle_alert(alert_id)
		elif request.values['submit'] == 'delete_alert':
			alert_id = request.form['id']
			result =delete_alert(alert_id)
			if result == 1:
				msg='Alarm has been deleted.'
				flash(msg,'success')
			elif result == 0:
				msg='Cannot delete the alarm.'
				flash(msg,'danger')

	alarms = show_alarms()
	reminders = show_reminders()
	count_alarms = alarms.count()
	count_reminders = reminders.count()
	return render_template('alarms.html' , page='Alarms & Reminders' , alarms=alarms , reminders=reminders , count_alarms = count_alarms , count_reminders = count_reminders)

@app.route("/appliances" , methods=['GET' , 'POST'])
def appliances_page():
	if 'user_id' not in session:
		return redirect(url_for('login_page'))
	elif request.method == 'POST':
		msg=None
		if request.form['submit'] == 'add_appliance':
			name = request.form['name']
			pin_number = request.form['pin_number']
			state = request.form['state']
			result=add_appliance(name , state , pin_number)
			if result==1:
				msg='Appliance added successfully.'
				flash(msg,'success')
			elif result==2:
				msg='Appliance with the same name already exists. Please use a different name.'
				flash(msg,'danger')
			elif result==0:
				msg='Pin Number is  already occupied. Please use a different pin.'
				flash(msg,'danger')
		elif request.values['submit'] == 'toggle':
			appliance_id = request.values['id']
			return toggle_appliance(appliance_id)
		elif request.values['submit'] == 'edit_appliance':
			id=request.form['id']
			name=request.form['name']
			pin_number=request.form['pin_number']
			state=request.form['state']
			result=update_appliance(id , name , pin_number , state)
			if result==1:
				msg='Appliance edited successfully.'
				flash(msg,'success')
			elif result==2:
				msg='Appliance with the same name already exists. Please use a different name.'
				flash(msg,'danger')
			elif result==0:
				msg='Pin Number is  already occupied. Please use a different pin.'
				flash(msg,'danger')
		elif request.values['submit'] == 'delete_appliance':
			id = request.form['id']
			result = delete_appliance(id)
			if result == 1:
				msg='Appliance is deleted from the list.'
				flash(msg,'success')
			elif result == 0:
				msg='Cannot delete the appliance.'
				flash(msg,'danger')
	appliances=show_appliances()
	count=appliances.count()
	return render_template('appliances.html' , page='Appliances' , appliances=appliances, count=count)

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
