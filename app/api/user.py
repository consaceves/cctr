from flask import Blueprint, jsonify, request, abort
from .. import models, db

app = Blueprint("user", __name__)

test_user = {
    "name": "name1",
    "user_id": 123,
    "dissability": ["arthritis", "als"]
}


@app.route('/user', methods=['GET', 'POST'])
def create_user():
    if not request.json:
        abort(400)
    
    if request.method=="POST":
        name = request.json.get("name")
        user_id = request.json.get("user_id")
        dissability = request.json.get("dissability")

        new_user = models.User(name=name,
                                user_id=user_id,
                                dissability=' '.join(map(str, dissability)))
        db.session.add(new_user)
        db.session.commit()
        return "User created"
    else: 
        user = models.User.query.filter_by(user_id=request.json["user_id"]).first()
        return jsonify(user_id=user.user_id,
                       name=user.name)