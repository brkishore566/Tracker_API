import requests
import random
import datetime
import time
import json

url = "http://127.0.0.1:5000/vitals_input"

Patient = { "user_id": 123, "timestamp": "", "heart_rate" : 45, "respiration_rate" : 18, "activity" : 3 }
user_id = 123
while True:
    heart_rate = random.randint(60,100)
    resp_rate =  random.randint(16,20)
    activity = random.randint(1,3)
    dt = datetime.datetime.now(datetime.timezone.utc)
    utc_time = dt.replace(tzinfo=datetime.timezone.utc)
    utc_timestamp = round(utc_time.timestamp())
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = [{"user_id" : user_id, "timestamp": utc_timestamp, "heart_rate" : heart_rate,\
            "respiration_rate" : resp_rate, "activity" : activity}]
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    time.sleep(1.0)

