from flask import Blueprint, jsonify, request, abort
from .. import models, db
from .workout import get_performance_score

app = Blueprint("user", __name__)

test_user = {
    "name": "name1",
    "user_id": 123,
    "disability": ["arthritis", "als"]
}

@app.route('/user', methods=['GET', 'POST'])
def create_user():
    if not request.json:
        abort(400)

    if request.method == "POST":
        name = request.json.get("name")
        user_id = request.json.get("user_id")
        disabilities = request.json.get("disabilities")
        blacklist = request.json.get("blacklist")
        age = request.json.get("age")
        gender = request.json.get("gender")

        pushups = request.json.get("pushups")
        situps = request.json.get("situps")
        mile = request.json.get("mile")
        pscore = get_performance_score(pushups, situps, mile)

        new_user = models.User(name=name,
                               user_id=user_id,
                               disabilities=' '.join(map(str, disabilities)),
                               blacklist=' '.join(map(str, blacklist)),
                               pscore=pscore)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({})
    else:
        user = models.User.query.filter_by(user_id=request.json["user_id"]).first()
        if user:
            return jsonify(user_id=user.user_id,
                           name=user.name)
        else:
            return jsonify({})