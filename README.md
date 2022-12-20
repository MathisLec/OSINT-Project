## DEPENDENCIES
- Shodan
- Requests
- ConfigParser

## Functioning
This tool can be use with the graphic interface, in command line or as an API.
To use the graphic interface:
```
$ graph.py
```
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