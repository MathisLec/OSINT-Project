import requests
import time
import os
import configparser as conf

URLSCAN_CONF_PATH = os.path.join(os.getcwd(),"resources","URLScan.conf")


c = conf.ConfigParser()
c.read(URLSCAN_CONF_PATH)

BASE_URL = "https://urlscan.io/api/v1/scan/"
HEADERS = {'API-Key' : c["DEFAULT"]["apiKey"]}

def scan(domain) :
    domain_info = requests.post (BASE_URL, data= {'url': domain}, headers= HEADERS)
    result_url = domain_info.json().get('api')
    is_done = False
    while not is_done:
        time.sleep(1)
        result = requests.get(result_url, headers=HEADERS).json()
        code = result.get ('status')
        if code != 404:
            is_done = True
    return result

