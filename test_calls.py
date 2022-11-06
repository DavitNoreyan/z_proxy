import requests
import json


def login():
    url = "https://imanage-prod.zerodemo.website/api/v1/session/login"
    data = {"user_id": "guestUser2", "password": "jU56yTFs", "persona": "user", "application_name": "Web Mobile"}
    response = requests.put(url, json=data, verify=False)
    json_response = response.json()
    token = json_response.get('X-Auth-Token')
    print(json_response)
    print(response.status_code)
    # process(token=token)


def process(token):
    url = "https://imanage-prod.zerodemo.website/api/v1/customs/custom2/search?offset=0&limit=50&scope=" \
          "performance&query_match_type=contains"
    d = {
        "X-Auth-Token": token,
        "Cookie": "IM_STATE_COOKIE=eyJ2ZXJzaW9uIjogIjAuMSJ9.Frqo3RytsSqhA96YeJ2auq-ADTs",
        "X-Login-Persona": "user"
    }

    response = requests.get(url=url, headers=d, verify=False)
    print(response.status_code)
    print(response.text)
    print(1111, response.headers)


login()
