## DEPENDANCES
## - TKinter
### Setup
#### Pre-Required
- python3-tk

#### Install
```
pip install tk
```

## - Shodan
#### Install
```
pip install shodan
```
## - Requests
#### Install
```
pip install requests
```

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

//

## URLSCAN

//

## Docker
docker build -t osint-img src_docker      