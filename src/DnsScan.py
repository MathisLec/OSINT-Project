import json
import os
import requests as http
import configparser as conf

DNSSCAN_JSON_PATH = os.path.join(os.getcwd(),"resources","example.json")
DNSSCAN_CONF_PATH = os.path.join(os.getcwd(),"resources","DnsScan.conf")

def urlFactory(domain):
    c = conf.ConfigParser()
    c.read(DNSSCAN_CONF_PATH)

    url = "https://www.whoisxmlapi.com/whoisserver/DNSService?"
    url += "apiKey="+c["DEFAULT"]["apiKey"]+"&"
    url += "domainName="+domain+"&"
    url += "type=_all"+"&"
    url += "outputFormat=JSON"

    return url


def scan(domain):
    r = http.get(url = urlFactory(domain))
    j = r.json()
    finalStr = ""
    dns = j["DNSData"]["dnsRecords"]
    for l in dns:
        finalStr += l["rawText"] + '\n'
    finalStr += "Nombre de services trouvés: "+str(len(dns))
    return finalStr

def scanL(domain):
    with open(DNSSCAN_JSON_PATH, 'r') as f:
        j = json.load(f)
        finalStr = "Name\t\t\tTTL\tClass\tType\tRessource\n"
        dns = j["dnsRecords"]
        for l in dns:
            finalStr += l["rawText"] + '\n'
        finalStr += "Nombre de services trouvés: "+str(len(dns))
    return finalStr