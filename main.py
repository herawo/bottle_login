from bottle import route, run
import login
import serving_static

@route('/')
def hello():
    return "<h1>Welcome</h1>\
    <a href='/login'><p>Connect</p></a>\
    "

run(host='localhost', port=8081, debug=True, reloader=True)
