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
from models.reply import Reply
from utils import obj_from_model

main = Blueprint('topic', __name__)


@main.route('/')
def index():
    ms = Topic.get_all()
    o = [obj_from_model(model) for model in ms]
    return jsonify(o)


@main.route('/detail', methods=["POST"])
def detail():
    id = int(request.get_json()["topic_id"])
    m = Topic.get(id)
    if m is not None:
        topicDetail = obj_from_model(m)
    else:
        topicDetail = {}
    rs = Reply.user_reply(topic_id=id)
    if rs is not None:
        replys = [obj_from_model(r) for r in rs]
    else:
        replys = []

    res = {
        "topicDetail": topicDetail,
        "replys": replys
    }
    return jsonify(res)


@main.route('/add', methods=["POST"])
def add():
    form = request.get_json()
    u = current_user()
    m = Topic.new(form, user_id=u.id)
    if m is not None:
        return jsonify({'type': '0', 'msg': '发布成功'})
    else:
        return jsonify({'type': '1', 'msg': '发布失败'})


@main.route('/delete', methods=["POST"])
def delete():
    pass