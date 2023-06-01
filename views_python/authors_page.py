from bottle import route, view


@route('/authors')
@view('about')
def home():
    return dict()
