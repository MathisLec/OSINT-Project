from shodan import Shodan

api = Shodan('M40ydHKH7Yh7lOVX2QPNu0cfFAdU8gif')

# Lookup an IP
def look_up_ip(ip: str) :
    ipinfo = api.host(ip)
    return(ipinfo)