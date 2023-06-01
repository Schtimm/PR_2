from bottle import route, view


@route('/breadth_first')
@view('breadth_first')
def breadth_first():
    return dict()
#@route("/gen_breadth_first_data")
#def gen_crascal_data():
#    """Генерация данных для решения"""
#    return alg_crascal.generate_matrix_to_solve()
