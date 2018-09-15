from bottle import route, run, request, template, redirect
import sqlite3

@route('/hello')
def hello():
    return "Hello World!"

@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            username: <input name="username" type="text" />
            password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
           '''

@route('/login', method='POST') 
def do_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	conn = sqlite3.connect('mydb.db')
	conn.text_factory = str
	c = conn.cursor()
	if check_id(c, username, "name"):
		if check_id(c, password, "password"):
			return template('templates/hello_template', name=username)
		else:
			return template('templates/error_template',error="Incorrect Password")
	else:
		return template('templates/error_template', error="Unknown Username")
		

def check_id(c, word, row):
	c.execute("SELECT "+ row +" FROM users")
	results = c.fetchall()
	for u in results :
		if ''.join(u) == word:
			return True
	return False

run(host='localhost', port=8080, debug=True, reloader=True)
