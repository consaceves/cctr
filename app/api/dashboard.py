from flask import Blueprint, jsonify, request

app = Blueprint("dashboard", __name__)

past_workouts = [
    {
        'id': 1,
        'title': "Exercise1",
        'description': "This is how you do Excercise1",
        'media': "This is the video/image of an example"

    },
    {
       'id': 2,
        'title': "Exercise2",
        'description': "This is how you do Excercise2",
        'media': "This is the video/image of an example" 
    }
]

@app.route('/dashboard', methods=['GET'])
def get_past_workouts():
    if not request.json or not 'user_id' in request.json:
        abort(400)
    return jsonify({'past_workouts': past_workouts})
