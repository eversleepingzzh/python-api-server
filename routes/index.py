from flask import (
    render_template,
    request,
    flash,
    redirect,
    url_for,
    session,
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
        user = u.__dict__
        del user["_id"]
        session["user_id"] = u.id
        session.permanent = True
        return jsonify(user)
    else:
        return jsonify({"msg": "密码或名字错误"})


@main.route('/register', methods=["POST"])
def register():
    form = request.get_json()
    # 完善逻辑
    if User.find_by(username=form["username"]) is None:
        u = User.register(form)
        if u is not None:
            return jsonify({"type": '0', "msg": "注册成功"})
        else:
            return jsonify({'type': '2', "msg": "系统故障，注册失败"})
    else:
        return jsonify({"type": '1', "msg": "该名字已经有人注册,请重新选择名字"})
