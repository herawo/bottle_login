from bottle import *
from users import User
import sqlite3
import hashlib
import macaron

install(macaron.MacaronPlugin("users.db"))

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='/home/clemalex/Documents/Project/bottle_login/static')

@route('/login')
def login():
	return template('templates/login_form_template')
	
@route('/register')
def login():
	return template('templates/register_form_template')
   
@route('/register', method='POST') 
def do_login():
	un = request.forms.get('username')
	pw = request.forms.get('password')
	h_pw = computeMD5hash(pw)
	User.create(username=un, password=h_pw)
	macaron.bake()
	redirect("/login")
 
@route('/login', method='POST') 
def do_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	password_hash = computeMD5hash(password)
	if check_id(username, password_hash):
		return template('templates/hello_template', name=username)
	else:
		return template('templates/error_template', error="Incorrect Password")
		
def check_id(username, password):
	try :
		usr = User.get("username=?",[username])
		if(usr):
			if(usr.password == password):
				return True
			else :
				return False
		else:
			return False
	except :
		return False

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

