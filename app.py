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



@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
