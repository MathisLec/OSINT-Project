import json
import os

def dnsScan():
    with open(os.path.join(os.getcwd(),"resources","example.json"), 'r') as f:
        j = json.load(f)
        dns = j["dnsRecords"]
        print("Nombre de services trouvés: "+str(len(dns)))
        for l in dns:
            print("Name: "+l["name"])
            print("Type: "+l["dnsType"])
            print("Raw text"+l["rawText"])
            print("")

def main():
    dnsScan()

main()