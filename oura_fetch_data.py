# Note for the user: 
# To access data such as heartrate, blood oxygen, sleep, etc., one just needs to change the URL to:
#  https://api.ouraring.com/v2/usercollection/______ <-- insert name of the data you want to access.

# This script will access the available oura data.

import requests
import json
import os



# Replace 'YOUR_PERSONAL_ACCESS_TOKEN' with your actual Oura personal access token
access_token = os.environ.get('PAT_Oura')

# Set the API endpoint for the data you want to retrieve (e.g., sleep data)
endpoints = {'heartrate': 'https://api.ouraring.com/v2/usercollection/heartrate',
            'sleep': 'https://api.ouraring.com/v2/usercollection/sleep',
            'activity': 'https://api.ouraring.com/v2/usercollection/daily_activity' ,
            'blood-o2': 'https://api.ouraring.com/v2/usercollection/daily_spo2'}

# Set up the headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}'
}

def fetch_data(endpoint):
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200: 
        return response.json()
    else: 
        print(f"Error fetching {endpoint}: {response.status_code} - {response.reason}")
        return None

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

sleep_data = fetch_data(endpoints['sleep'])
if sleep_data:
    save_to_json(sleep_data, 'sleep.json')
    print('Sleep data has successfully saved to sleep.json')

heartrate_data = fetch_data(endpoints['heartrate'])
if heartrate_data: 
    save_to_json(heartrate_data, 'heartrate.json')
    print('Heart rate data has successfully saved to heartrate.json')

blood_o2_data = fetch_data(endpoints['blood-o2'])
if blood_o2_data: 
    save_to_json(blood_o2_data, 'blood-o2.json')
    print('Blood-o2 data has successfully saved to blood-o2.json')

activity_data= fetch_data(endpoints['activity'])
if activity_data: 
    save_to_json(activity_data, 'activity.json')
    print('Activity data has successfully saved to activity.json')






