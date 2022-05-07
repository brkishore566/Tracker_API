# Tracker_API
heart rate and respiration rate tracker API

Assumptions made:
* Assuming the data is sent automated from the wearable device. incoming data is correct (type checking is not done)
* if user doesnt provide the parameter **time_frame** by default it is considered 15 mins time frame.
* if user provides the parameter **time_frame** data aggretaion is done in the range of **time_frame**.
* user_id is considered as **123** as it is being sent from the same device. solution can be extended if it is used for multiple user_id's. filter in the get request and incorporating the same on dataframe.
* aggregation is done in hourly manner(according to the time_frame provided) from the first time stamp record found in the data frame.
*
