from flask import (
    render_template,
    request,
    flash,
    redirect,
    url_for,
    jsonify,
    Blueprint,
)
from routes import *
from models.topic import Topic

main = Blueprint('topic', __name__)


@main.route('/')
def index():
    pass


@main.route('/<int:id>')
def detail(id):
    m = Topic.get(id)


@main.route('/add', methods=["POST"])
def add():
    form = request.get_json()
    m = Topic.new(form)
    return jsonify({'msg': 111111})


@main.route('/delete', methods=["POST"])
def delete():
    pass