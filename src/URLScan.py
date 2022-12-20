import requests
import time
import os
import configparser as conf
import json
import traceback

URLSCAN_CONF_PATH = os.path.join(os.getcwd(),"resources","URLScan.conf")


c = conf.ConfigParser()
c.read(URLSCAN_CONF_PATH)
API_KEY = c["DEFAULT"]["apiKey"]

BASE_URL = "https://urlscan.io/api/v1/scan/"
HEADERS = {'API-Key' : API_KEY, 'Content-Type': 'application/json'}

def scan(domain) :
    domain_info = requests.post(BASE_URL, headers= HEADERS, data=json.dumps({'url': domain, 'visibility': 'public'}))
    result_url = domain_info.json()
    try:
        result_url = result_url["api"]
    except KeyError:
        return result_url["description"]
    is_done = False
    while not is_done:
        time.sleep(1)
        result = requests.get(result_url, headers=HEADERS).json()
        code = result.get ('status')
        if code != 404:
            is_done = True
    return json.dumps(result, indent=4)

