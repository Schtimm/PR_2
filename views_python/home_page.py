# Автор: Панков Василий
# Дата создания: 27.05.2023


from json import dump, load
from re import fullmatch

from bottle import route, view, request, redirect
from typing import Dict, List, Tuple


def mail_is_correct(mail: str):
    """Проверка почты на корректность

    :param mail: почта
    :rtype: bool or None
    :return возвращает корректна ли почта или нет
    """
    return fullmatch(r"[a-zA-Z0-9._&=‘\-+]{1,256}@[a-zA-Z0-9]{1,100}\.[a-zA-Z]{1,7}", mail) is not None


@route('/')
@route('/home')
@view('index')
def home():
    """Домашняя страница"""
    message = ""
    is_error = False
    try:
        message = request.query.message
        is_error = bool(request.query.is_error)
    except Exception:
        pass

    return dict(is_error=is_error, message=message)


# Переменная в которой лежат вопросы, пользователей
questions: Dict[str, List[Tuple[str, str]]] = {}


def save_questions():
    """Запись в файл всех вопросов из переменной questions"""
    with open("questions.json", "w", encoding="utf-8") as f:
        dump(questions, f)


def load_questions():
    """Загрузка вопросов из файла в переменную questions"""
    global questions
    try:
        with open("questions.json", "r", encoding="utf-8") as f:
            questions = load(f)
    except FileNotFoundError:
        save_questions()


# Обработка формы взята из прошлой работы
@route("/send_message", method="post")
def get_message():
    """Обработка формы"""
    mail: str = request.forms.get('email')
    username: str = request.forms.get('name')
    quest: str = request.forms.get("message")
    # проверка на пустоту
    if mail.strip() == "" or username.strip() == "" or quest.strip() == "":
        return redirect("/?message=Некоторые поля не заполнены&is_error=True#message_form")
    # проверка на корректность почты
    if not mail_is_correct(mail):
        return redirect("/?message=Введённая почта некорректна&is_error=True#message_form")

    # загрузка вопросов из файла
    load_questions()
    # проверка, является ли почта новой
    if mail not in questions:
        questions[mail] = [(username, quest)]
    else:
        # есть ли вопрос дубликат
        for el in questions[mail]:
            if el[1] == quest:
                return redirect("/?message=Ваш вопрос уже был отправлен&is_error=True#message_form")
            # если нет то добавляем
            questions[mail].append((username, quest))
        # сохранение вопросов в файл
    save_questions()
    return redirect("/?message=Ваше сообщение отправлено#message_form")
