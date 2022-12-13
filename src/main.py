#!/usr/bin/env python3
# -*- coding:Utf-8 -*-
import sys
import os
import getopt
import DnsScan

SCAN_DICT = {"dnsscan": 0, "shodan":0, "theharvester":0, "urlscan":0}
URL_DOMAIN = ""

def usage():
    print("usage: main.py FLAG DOMAIN\n")
    print("FLAG:\n")
    print("-h, --help\n\tshow this help")
    print("-d, --dnsscan\n\tactiv the dnsscan")
    print("-s, --shodan\n\tactiv the shodan scan")
    print("-t, --theharvester\n\tactiv the thehavester scan")
    print("-u, --urlscan\n\tactiv the urlscan")
    print("DOMAIN:\n")
    print("--domain "+"\x1B[3m"+"\u0332".join("URL")+"\x1B[0m"+"\n\tthe url domain to attack")

def write(file_name, txt):
    with open(os.path.join(os.getcwd(),"resources","example.json"), 'w+') as f:
        f.write(txt)

def main(argv):
    try:
        opts,args = getopt.getopt(argv,"hdstu",["help","dnsscan", "shodan", "theharvester", "urlscan", "domain="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h","--help"):
            usage()
            sys.exit(2)
        elif opt in ("-d","--dnsscan"):
            SCAN_DICT["dnsscan"] = 1
        elif opt in ("-s","--shodan"):
            SCAN_DICT["shodan"] = 1
        elif opt in ("-t","--theharvester"):
            SCAN_DICT["theharvester"] = 1
        elif opt in ("-u","--urlscan"):
            SCAN_DICT["urlscan"] = 1
        elif opt == "--domain":
            URL_DOMAIN = arg
        
    '''    
    if not os.path.exists(repertoire):
        os.makedirs(repertoire)
    DnsScan.scanL("www.google.fr")
'''
if __name__ == "__main__":
    main(sys.argv[1:])