from bottle import route, view


@route('/authors')
@view('authors')
def home():
    return dict()
