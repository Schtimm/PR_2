from bottle import route, view
@route('/')
@route('/home')
@view('home')
def home():
    return dict()