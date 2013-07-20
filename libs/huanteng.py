import requests
import json

TOKEN_KEY = "yKCP9K6vRm7dduNEWnxC"
SIGN_IN_URL = "https://huantengsmart.com/users/sign_in.json"
URL = "https://huantengsmart.com/humidity_data/11.json?start=15_min_ago&auth_token=%s"
USER = "hackathon2@huantengsmart.com"
PASS = "h4o9ba"


def get_token(username, passwd):
    payload = {
        "user": {
            "email": username,
            "password": passwd
        }
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(SIGN_IN_URL, data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        data = r.json()
        return data["auth_token"] if data["success"] == True else None


def get_huminity(token):
    if not token:
        return None
    r = requests.get(URL % token)
    if r.status_code == 200:
        data = r.json()
        data = data["th_sensor"]
        data = data["current_humidity"]
        return data


if __name__ == '__main__':
    t = get_token(USER, PASS)
    print get_huminity(t)
