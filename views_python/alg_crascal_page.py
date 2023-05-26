from bottle import route, view


@route('/crascal')
@view('alg_crascal')
def home():
    return dict()
