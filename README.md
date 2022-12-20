## DEPENDENCIES
- Shodan
- Requests
- ConfigParser
- JsonLib
### Install
```bash
pip install -r requirements.txt
```

## Functioning
This tool can be use with a graphic interface, in command line or as an API.
To use the graphic interface:
```
$ graph.py
```
You can click on the button of the scan that you want to perform, enter the domain to OSINT in the text area, then click on the Start Button.
Once completed, the results can be consulted in the next view by select the report that you want to see. It takes some time, don't worry.

To use this tool in command line:
```
$ main.py FLAG URL
```
You can get the flag list with -h argument.
Finally, it can be use as API by giving a dictionnary such as
```python
{"DnsScan": 0, "Shodan":0, "TheHarvester":0, "URLScan":0}
```
and URL to the main(URL, scans) function in main.py, wich 0 say that the scan is disabled, and 1 when it is enabled.
```
usage: main.py FLAG DOMAIN

FLAG:

-h, --help
        show this help
-d, --dnsscan
        activ the dnsscan
-s, --shodan
        activ the shodan scan
-t, --theharvester
        activ the thehavester scan
-u, --urlscan
        activ the urlscan
DOMAIN:

--domain URL
        the url domain to attack
```

Because we use API in out application, we store API Keys in conf files on the resources directory, which are imported in the different scans.
You can use the function scanL(domain) in DnsScan.py script to limit the query API usage. It parse local json file instead of HTTP response from the API.

## DNSSCAN
We are using the API service dns-lookup from whoisxmlapi.com

## SHODAN
We are using official python library for Shodan
https://github.com/achillean/shodan-python

## THEHARVESTER
Not implemented yet

## URLSCAN
We are using the API service urlscan.io https://urlscan.io/

# EXTRA
## Docker
Out application can be contenerised using DockerFile in src_docker directory as followed:
```bash
$ docker build -t osint-img src_docker
```
This command will build the image and add it to your images list.
It may be used as followed:
```
docker run -e dnsscan= -e domain="www.jambon.fr" -v $(pwd):/code/scans osint-img:latest
```
To enable scans that you want, add the environment variable among:
- dnsscan=
- shodan=
- theharvester=
- urlscan=

Then, you must include the domain that you want perform the test:
```
-e domain=<domain>
```
The scans output are writed in the directory /code/scans in the container. So, in order to retrieve them, you must mount a volume toward that path.