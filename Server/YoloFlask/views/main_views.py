# Blueprint : URL과 그에 맞는 함수 관계를 확인할려고 씀.

from flask import Blueprint

# 'main' 함수명으로 url 찾는 url_for 함수에 사용됨
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_py():
    return 'Hello, py!'


@bp.route('/')
def index():
    return 'Pybo index'
