from bottle import route, view


@route('/breadth_first')
@view('breadth_first')
def home():
    return dict()
