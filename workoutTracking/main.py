import requests
from datetime import datetime
import os

USERNAME = "Ismet"
PASSWORD = "workoutTracking#51"

GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 187
AGE = 24

APP_ID = "546acc44"
API_KEY = "de044c88b76aeecdca50bd5355777a2a"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/e3791f2c32af7bca59a11e08361538ad/workoutTracking/workouts"


exercise_text = input("Tell me which exercises you did today: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result_data = response.json()


today_date = datetime.now().strftime("%Y%m%d")
now_time = datetime.now().strftime("%X")

for exercise in result_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(USERNAME, PASSWORD))







