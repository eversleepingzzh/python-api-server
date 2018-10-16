from flask import (
    render_template,
    request,
    flash,
    redirect,
    url_for,
    jsonify,
    Blueprint,
)
from models.user import User
main = Blueprint('index', __name__)


@main.route('/login', methods=["POST"])
def login():
    form = request.get_json()
    u = User.validate_login(form)
    if u is not None:
        return jsonify({"msg": "success"})
    else:
        return jsonify({"msg": "fail"})

@main.route('/register', methods=["POST"])
def register():
    form = request.get_json()
    print(form)
    u = User.register(form)
    if u is not None:
        return jsonify({"msg":'1'})
    else:
        return jsonify({'msg': '2'})