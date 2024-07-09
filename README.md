# Py-Oura-Api-Client
Purpose: Setup Python client for the Oura API to extract data onto a json

Note: DM me for the PAT since you need to store PAT in an environment variable. 

Run this command in python3 terminal: 
pip install requests 

heartrate.json contains heart rate data (data can be pulled continuously anytime)
blood-o2.json contains blood oxygen data (data can only be pulled after the person sleeps for 3+ hrs)
activities.json contains data summarizing the person's activity levels (e.g. target calories, total calories, resting time, etc.)
sleep.json contains data about how the person slept (data can only be pulled after the person takes a nap, say more than 15 mins) 

7/8: Looking to pull more data from the oura ring sensors in the near future, for now only sleep, heart rate, activities, and blood o2 are accounted for. 


