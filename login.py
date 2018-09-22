from bottle import route, request, template, redirect
import sqlite3
import hashlib
from bottle import static_file

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='/home/clemalex/Documents/Project/bottle_login/static')

@route('/login')
def login():
    return template('templates/login_form_template')
    
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
	conn = sqlite3.connect('mydb.db')
	conn.text_factory = str
	c = conn.cursor()
	c.execute("SELECT name FROM users")
	results = c.fetchall()
	for u in results :
		if ''.join(u) == username:
			c.execute("SELECT password FROM users where name= ? ", (username,))
			results = c.fetchall()
			for u in results :
				if ''.join(u) == password:
					return True
				else :
					return False
		else :
			return False

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

