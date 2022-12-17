from Shodan import look_up_ip
import os
import json
import socket

def main () :
    ip = socket.gethostbyname("www.google.com")
    print(ip)
    host = ip
    shodan_info=look_up_ip(host)
    save_file (host, 'shodan.json', json.dumps(shodan_info, indent=4))

def save_file(folder : str, filename : str, content : str):
    path= f'{folder}/{filename}'
  

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)




main()