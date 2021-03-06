from flask import Blueprint, jsonify, request, abort
from .. import models

app = Blueprint("workout", __name__)

walking = ['walking', 'quads', 'hamstrings']
biking = ['biking', 'quads', 'hamstrings']
swimming = ['swimming', 'shoulders']
elliptical = ['elliptical']
resistance_bands = ['resistance_bands']
bench_press = ['bench press', 'pecs', 'triceps', 'delts', 'elbow', 'wrists', 'hands', 'shoulders']
running = ['running', 'knees', 'quads', 'hamstrings']
stair_climbing = ['stair_climbing', 'knees', 'quads', 'hamstrings']
pushups = ['pushups', 'pecs', 'triceps', 'abs', 'delts', 'elbows', 'wrists', 'shoulders']
lunges = ['lunges', 'quads', 'hamstrings', 'glutes', 'hips', 'knees']
sit_ups = ['sit_ups', 'abs']
dips = ['dips', 'triceps', 'pecs', 'elbows', 'shoulders']
weight_machines = ['weight_machines']
knee_extensions = ["knee_extensions", "knees", 'quads', 'hamstrings']
squats = ['squats', 'quads', 'glutes', 'hips', 'abs', 'calves', 'hamstrings', 'back', 'knees']
yoga = ['yoga']
tai_chi = ['tai_chi']
gardening = ['gardening', 'back', 'shoulders']
calf_raises = ['calf_raises', 'calves', 'ankles']
leg_raises = ['leg_raises', 'hips', 'abs', 'quads', 'hamstrings']
arm_stretch = ['arm_stretch', 'elbow']
leg_stretch = ['leg_stretch', 'quads', 'hamstrings', 'knees']
hip_stretch = ['hip_stretch']

glute_bridges = ['glute_bridges', 'hips', 'abs', 'glutes', 'hamstrings', 'quads', 'knees']
arm_circles = ['arm_circles', 'shoulders']
rowing = ['rowing', 'elbows', 'knees', 'shoulders', 'quads', 'hamstrings', 'hands']

# categories

cardio = [walking, biking, swimming, stair_climbing, elliptical, running, rowing]
low_impact = [walking, biking, swimming, elliptical, weight_machines, resistance_bands, glute_bridges, arm_circles,
              yoga, tai_chi, arm_stretch, hip_stretch, leg_raises, leg_stretch, calf_raises, gardening, sit_ups]
body_weight = [pushups, sit_ups, lunges, yoga, tai_chi, glute_bridges]
flexibility = [yoga, tai_chi, arm_stretch, leg_stretch, hip_stretch, arm_circles]
strength = [bench_press, squats, pushups, lunges, sit_ups, weight_machines, resistance_bands, glute_bridges]
mind_and_body = [yoga, tai_chi]
functionality = [walking, stair_climbing, gardening, knee_extensions, arm_circles]

rep_based = [resistance_bands, bench_press, pushups, lunges, sit_ups, dips, weight_machines, knee_extensions,
             calf_raises, leg_raises, glute_bridges, arm_circles]
time_based = [walking, biking, swimming, elliptical, running, yoga, tai_chi, gardening, arm_stretch, leg_raises,
              hip_stretch, rowing]

rep_based_exercises = ['resistance_bands', 'bench_press', 'pushups', 'lunges', 'sit ups', 'dips', 'weight_machines',
                       'knee_extensions', ' calf_raises', 'leg_raises', 'glute bridges', 'arm_circles']
time_based_exercises = ['walking', 'biking', 'swimming', 'elliptical', 'running', 'yoga', 'tai_chi', 'gardening',
                        'arm_stretch', 'leg_stretch,', 'leg_raises', 'hip_stretch', 'rowing']
# Arthritis
arthritis_affected = ['knees', 'hands', 'wrists', 'elbows']
arthritis_needs = [cardio, low_impact, strength, flexibility, mind_and_body]

# ALS
als_affected = ['hands']
als_needs = [flexibility, cardio]

# Muscular Dystrophy
muscular_dystrophy_affected = []
muscular_dystrophy_needs = [flexibility, cardio, strength, functionality]

# Osteoporosis
osteoporosis_affected = []
osteoporosis_needs = [strength, body_weight, flexibility, cardio]

# Parkinsons
parkinsons_affected = []
parkinsons_needs = [cardio, flexibility, functionality]

def get_workout(input):

    recommended_exercises = get_intersections(input.disabilities.split(' '), input.blacklist.split(' '))
    result = get_recommended_workout(recommended_exercises, input)
    return result

def intersection(lst1, lst2):
    # Use of hybrid method
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


def get_exercises(disability, blacklist):
    result = {}
    if disability == 'als':
        affected = als_affected
        needs = als_needs
    elif disability == 'arthritis':
        affected = arthritis_affected
        needs = arthritis_needs
    elif disability == 'md':
        affected = muscular_dystrophy_affected
        needs = muscular_dystrophy_needs
    elif disability == 'osteoporosis':
        affected = osteoporosis_affected
        needs = osteoporosis_needs
    else:
        affected = parkinsons_affected
        needs = parkinsons_needs

    for category in needs:
        # print("category: " + str(category))
        for exercise in category:
            # print("exercise: " + str(exercise))
            # print("affected: " + str(affected))
            # print("intersection: " + str(intersection(affected, exercise)))
            if len(intersection(affected, exercise)) == 0 and len(intersection(exercise, blacklist)) == 0:
                exercise_name = exercise[0]
                if exercise_name in result:
                    result[exercise_name] = result[exercise_name] + 1
                else:
                    result[exercise_name] = 1

    # sort by values
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    # print(result)

    exercise_list = []
    for tuple in result:
        exercise_list.append(tuple[0])
    return exercise_list


def get_recommended_workout(recommended_exercises, input):
    result = {}
    #user_profile = jsonify(input)
    user_profile = {x.name: getattr(input, x.name) for x in input.__table__.columns}
    for exercise in recommended_exercises:
        intensity = get_intensity(input.pscore)
        #print(user_profile[exercise])
        #print(intensity)
        currentIntensity = user_profile[exercise]
        #maxIntensity = max(currentIntensity, intensity[0])
        if exercise in rep_based_exercises:
            result[exercise] = " 3 sets of " + str(max(currentIntensity, intensity[0]))
        else:
            result[exercise] = str(max(currentIntensity, intensity[1])) + " minutes"
        #result[exercise] = str(maxIntensity) + " minutes"

    return result


def get_intersections(disabilities, blacklist):
    exercises = []
    for disability in disabilities:
        exercises.append(get_exercises(disability, blacklist))

    result = exercises[0]
    for exercise in exercises:
        result = intersection(result, exercise)

    return result


def get_performance_score(pushups, situps, mile_time):
    pscore = (100.0 / 60) * (pushups + 1.0 * situps / 2 + 20 * 11.0 / mile_time)
    # print(pscore)
    return pscore


def get_intensity(pscore):
    if pscore > 110:
        return [7, 11]
    elif pscore < 90:
        return [5, 9]
    else:
        return [6, 10]





# Example input
# Expecting input in this form, or similar with the same keys
# Make sure keys are spelled correctly, and note the space in push up and sit up
input = {'disabilities' : ['md'], 'blacklist' : ['knees', 'elbows'], 'push ups' : 20, 'sit ups' : 40, 'mile' : 10}


user_profile = {'disabilities': input['disabilities'], 'blacklist' : input['blacklist'], 'age': 0, 'pscore': get_performance_score(input['push ups'], input['sit ups'], input['mile']), 'walking': 0, 'biking': 0,
                    'swimming': 0, 'elliptical': 0, 'resistance bands': 0, 'bench press': 0, 'running': 0,
                    'stair climbing': 0, 'pushups': 0, 'lunges': 0, 'sit ups': 0, 'dips': 0, 'weight machines': 0,
                    'knee extensions': 0, 'squats': 0, 'yoga': 0, 'tai chi': 0, 'gardening': 0, 'calf raises': 0,
                    'leg raises': 0, 'arm stretch': 0, 'leg stretch': 0, 'hip stretch': 0, 'glute bridges': 0,
                    'arm circles': 0, 'rowing': 0}

# FOR DEMO
example_result = {'arm circles': ' 3 sets of 6', 'walking': '10 minutes', 'yoga': '10 minutes', 'tai chi': '10 minutes', 'arm stretch': '10 minutes', 'hip stretch': '10 minutes', 'biking': '10 minutes', 'swimming': '10 minutes', 'elliptical': '10 minutes', 'bench press': '10 minutes', 'sit ups': ' 3 sets of 6', 'weight machines': ' 3 sets of 6', 'resistance bands': '10 minutes', 'gardening': '10 minutes'}

#result = get_workout(input)
#print(result)

@app.route('/workout', methods=['GET'])
def get_new_workout():
    if not request.json:
        abort(400)

    else:
        # FIX GET JSON FUNCTION I forgot what it was called lol
        #input = get.json()
        user = models.User.query.filter_by(user_id=request.json['user_id']).first()
        result = get_workout(user)
        return jsonify(result)