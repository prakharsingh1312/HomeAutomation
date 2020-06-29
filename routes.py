
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
	return render_template('appliances.html' , page='Appliances')

@app.route("/user")
def user_page():
	if 'user_id' not in session:
		return redirect(url_for('login_page'))
	user=get_user_details()
	return render_template('User_profile.html' , page='User Profile' , user=user)
