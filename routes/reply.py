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
from models.reply import Reply
from utils import obj_from_model

main = Blueprint('reply', __name__)


@main.route('/add', methods=["POST"])
def add():
    form = request.get_json()
    u = current_user()
    t = Reply.new(form, user_id=u.id)
    return jsonify({'msg': 'maybe'})
