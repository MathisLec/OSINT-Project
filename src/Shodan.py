from shodan import Shodan
import socket
import json
import os
import configparser as conf

SHODAN_CONF_PATH = os.path.join(os.getcwd(),"resources","Shodan.conf")

c = conf.ConfigParser()
c.read(SHODAN_CONF_PATH)

api = Shodan(c["DEFAULT"]["apiKey"])

# Lookup an IP
def scan(domain) :
    host = socket.gethostbyname(domain)
    response = api.host(host)
    finalStr = json.dumps(response, indent=4, separators=('\t',':\t'))
    finalStr = finalStr.replace("{", "")
    finalStr = finalStr.replace("}", "")
    finalStr = finalStr.replace("[", "")
    finalStr = finalStr.replace("]", "")
    finalStr = finalStr.replace('"', "")
    return(finalStr)