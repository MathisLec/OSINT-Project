from Shodan import look_up_ip
import os
import json
from urlscan import scan_domain

def main () :
    host = '8.8.8.8'
    #shodan_info=look_up_ip(host)
    #save_file (host, 'shodan.json', json.dumps(shodan_info, indent=4))

    url_scan_info = scan_domain(host) 
    save_file (host, 'url_scan.json', json.dumps(url_scan_info, indent=4))


def save_file(folder : str, filename : str, content : str):
    path= f'{folder}/{filename}'
  

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)




main()