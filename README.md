# Tracker_API

heart rate and respiration rate tracker API

Assumptions made:
* Assuming the data is sent automated from the wearable device. incoming data is correct (type checking is not done)
* if user doesnt provide the parameter **time_frame** by default it is considered 15 mins time frame.
* if user provides the parameter **time_frame** data aggretaion is done in the range of **time_frame**.
* user_id is considered as **123** as it is being sent from the same device. solution can be extended if it is used for multiple user_id's. filter in the get request and incorporating the same on dataframe.
* aggregation is done in hourly manner(according to the time_frame provided) from the first time stamp record found in the data frame.
* File simulator.py is used to write vital record of the patient to the csv file every second by calling the API
* url http://127.0.0.1:5000/vitals_output gives aggregated data with 15 mins time frame.
* url http://127.0.0.1:5000/vitals_output?time_frame=30 gives aggregated data with 30 mins time frame. time frame should be greater than 0 and less than 60.
* url http://127.0.0.1:5000/vitals_input is used to post the data to the csv. below is the payload(can take multiple inputs as well):

[{
    "user_id": "123",
    "timestamp": "1587631419",
    "heart_rate": "45",
    "respiration_rate": "18",
    "activity": "3"
}] 

* make sure the the csv file exists and chnage the path of csv accordingly.
* **user_vitals.csv** has the data which is simulated via **simulator.py**.
* aggregated data can be obtained by calling the api end point http://127.0.0.1:5000/vitals_output?time_frame=30

if you are trying to execute this api. start the local server for flask api(default port 5000), run simulator.py (it will be running infinitely populating values to the api) you can stop it whenever necessary. for testing purpose i did some tests for time_frame in seconds which is what can be found in the csv file in this repo.

below are the screen shots of API calls and process:

1. Post vitals:
<img width="896" alt="Screenshot 2022-05-08 at 12 23 24 AM" src="https://user-images.githubusercontent.com/47842664/167268261-3f53cc0c-989c-481d-ab16-4831c74ac898.png">


2. read aggregated data for default time frame of 15 mins
<img width="898" alt="Screenshot 2022-05-08 at 12 23 56 AM" src="https://user-images.githubusercontent.com/47842664/167268270-3f25f83b-6c3a-44a3-83b7-98f6b59480f4.png">


3. read aggregated data for time frame of 30 mins
<img width="894" alt="Screenshot 2022-05-08 at 12 28 32 AM" src="https://user-images.githubusercontent.com/47842664/167268276-9c5cf53a-66a4-4cfd-a3a5-850289c9d20c.png">

