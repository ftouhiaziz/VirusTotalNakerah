# VirusTotalNakerah
A simple Python-based command-line script to interact with virustotal-api.
***********
URL Scan
Submit URL(s) to be scanned.


python vt_driver.py url-scan [-h] url [url ...]

******
Positional arguments:

url         URL(s) (up to 25)



Optional arguments:

-h, --help  Show this help message and exit

***************
URL Report


Get URL scan results.

python vt_driver.py url-report [-h] url [url ...]

****
Positional arguments:


url         URL(s) (up to 25)


Optional arguments:

-h, --help  Show this help message and exit

**************
IP Report

Get information about an IP address.

python vt_driver.py ip-report [-h] ip
****
Positional arguments:
 ip          An IPv4 address
 ****


Optional arguments:
 -h, --help  Show this help message and exit

***************
Domain Report

Get information about a domain.

python vt_driver.py domain-report [-h] domain
****
Positional arguments:
 domain      A domain name
 ****
Optional arguments:
 -h, --help  Show this help message and exit
