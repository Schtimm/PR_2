# Автор: Панков Василий
# Дата создания: 27.05.2023

from bottle import route, view, request, redirect
from typing import List

from logic import alg_crascal


@route('/crascal')
@view('alg_crascal')
def home():
    return dict(matrix="", graph="graph LR\nТут -- будет --- A[ваш граф]", solve=[], error="")


@route("/crascal", method="post")
@view('alg_crascal')
def solve_crascal():
    matrix: List[List[float]]
    string_matrix = ""
    try:
        string_matrix = request.forms.matrix
        matrix = alg_crascal.parse_matrix_from_string(string_matrix)
    except KeyError:
        # Этот вариант возможен только под воздействием другого разработчика на страницу
        return dict(matrix=string_matrix, graph="graph LR\nТут -- будет --- A[ваш граф]",
                    error="Что-то пошло не так, вы кидаете пустые POST запросы", solve=[])
    except ValueError:
        # Парсинг матрицы неудачный
        return dict(matrix=string_matrix, graph="graph LR\nТут -- будет --- A[ваш граф]",
                    error="В вашем графе содержатся буквы или иные некорретные символы", solve=[])

    try:
        solve = list(alg_crascal.crascal_solve_with_steps(matrix))
    except AssertionError as e:
        # Если сработади дополнительные проверки
        return dict(matrix=string_matrix, graph="graph LR\nТут -- будет --- A[ваш граф]",
                    error=e.__str__(), solve=[])
    except Exception as e:
        #  Если что-то произошло иное
        print(e.__str__)
        return redirect("/crascal")
    return dict(matrix=string_matrix, graph=solve[0]["graph"], solve=solve, error="")
