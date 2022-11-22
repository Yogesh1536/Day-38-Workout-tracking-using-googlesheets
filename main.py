import requests
from datetime import datetime

API_ID = "68e2cb8f"
API_KEY = "14b10d1ac5c21fedbfd8a1c2409f3490"
USER_NAME = "Yogesh"
USER_PASSWORD = "yogesh$workout$tracking"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f67b10a3d7cc6477d8bac06b1ce12143/workoutTracking/workouts"

user_writen = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

exercise_param = {
    "query": user_writen,
    "gender": "male",
    "weight_kg": 67.8,
    "height_cm": 178.80,
    "age": 23
}

response = requests.post(url=exercise_endpoint, json=exercise_param, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    new_rows = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=new_rows, auth=(USER_NAME, USER_PASSWORD))
    print(sheet_response.text)