from flask import Blueprint, jsonify, request, abort

app = Blueprint("workout", __name__)

new_workout = [{"exercise": "tai-chi", "time": "8 min"}, {"exercise": "yoga", "time": "8 min"}]

@app.route('/workout', methods=['GET'])
def get_new_workout():
    if not request.json:
        abort(400)
    # call richard's script here, return array of exercises
    return jsonify({'new_workout': new_workout})