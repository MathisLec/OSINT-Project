import requests
import time
base_Url = "https://urlscan.io/api/v1/scan/"
headers = {'API-Key' : 'ce7ec812-1458-4bcf-bdeb-2359893736a9'}

def scan_domain (domain : str) :

    domain_info = requests.post (base_Url, data= {'url': domain}, headers= headers)
    result_url = domain_info.json().get('api')
    print (result_url)
    is_done = False
    while not is_done:
        time.sleep (10)
        result = requests.get(result_url, headers=headers).json()
        code = result.get ('status')
        if code != 404:
            is_done = True
    return result

