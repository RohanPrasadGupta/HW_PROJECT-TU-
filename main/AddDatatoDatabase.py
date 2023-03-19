import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-detection-project-29f3d-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "121":
        {
            "name": "KYAW THIHA",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "122":
        {
            "name": "ADNAN ALI",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "123":
        {
            "name": "DARIO ELLIS",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "B+",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "124":
        {
            "name": "ROHAN PRASAD GUPTA",
            "major": "AI and IoT",
            "starting_year": 2022,
            "total_attendance": 79,
            "standing": "A",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
 }

for key, value in data.items():
    ref.child(key).set(value)