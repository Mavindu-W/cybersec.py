# cybersec.py
Automate the process of scanning for live hosts and checking for vulnerabilities.
# CyberSec URL Scanner and ZAP Automation

## Overview
This project is designed to automate the process of checking the availability of a list of URLs and then performing security scans on the live URLs using OWASP ZAP (Zed Attack Proxy). The scanning process includes spidering the target URLs and performing both active and passive scans to identify potential security vulnerabilities.

## Features
- **URL Availability Check**: The script first checks if the URLs from the provided list are live and accessible.
- **Automated Security Scanning**: For each live URL, the OWASP ZAP tool is used to perform in-depth security scans, including spidering and active scanning.
- **Report Generation**: After scanning each URL, a detailed report is generated in HTML format for review.
- **Multiple Protocol Support**: The script handles both HTTP and HTTPS URLs.

## Requirements
Before running the script, ensure you have the following installed:
- Python 3.x
- OWASP ZAP (in daemon mode)
- Docker (for ZAP execution)
- Python packages:
  - `requests`
  - `beautifulsoup4`
  - `prettytable`
  - `alive-progress`
  - `zapv2`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mavindu-W/cybersec.py.git
   cd cybersec
   pip3 install -r requirements.txt
   python3 cybersec.py -h 

## HELP

┌──(mavindu㉿kali)-[~/Desktop/full_zapscan]
└─$ python cybersec.py -u urls.txt
---------------------------------------------------------------------------------------------------------------
------------ | Automate the scan for checking live hosts and vulnerabilities.| --------------
---------------------------------------------------------------------------------------------------------------
 /  __ \     | |             /  ___|          
| /  \/_   _| |__   ___ _ __\ `--.  ___  ___ 
| |   | | | | '_ \ / _ \ '__|`--. \/ _ \/ __|
| \__/\ |_| | |_) |  __/ |  /\__/ /  __/ (__ 
 \____/\__, |_.__/ \___|_|  \____/ \___|\___|
        __/ |                                
       |___/                                 
                                      V 0.1
        ---------------------|by Mavindu_Wijesekara
-------------------------------------------------------------
on 0: Starting ZAP scan for http://tab-ajc-qa-trade-universal.directfn.net
on 0: Starting spider scan on: http://tab-ajc-qa-trade-universal.directfn.net
on 0: Spider scan progress: 0%
on 0: Spider scan progress: 90%
on 0: Spider scan completed
on 0: Starting active scan on: http://tab-ajc-qa-trade-universal.directfn.net
on 0: Active scan progress: 0%
on 0: Active scan progress: 12%
on 0: Active scan progress: 12%
on 0: Active scan progress: 12%
on 0: Active scan progress: 12%
on 0: Active scan progress: 23%
on 0: Active scan progress: 23%
on 0: Active scan progress: 38%
on 0: Active scan progress: 38%
on 0: Active scan progress: 38%
on 0: Active scan progress: 39%
on 0: Active scan progress: 39%
on 0: Active scan progress: 39%
on 0: Active scan progress: 40%
## TEST RUN

on 1: Generating report for http://tab-alawwal-qa-trade-universal.directfn.net at /home/mavindu/Desktop/full_zapscan/reports/tab-alawwal-qa-trade-universal.directfn.net_report.html
on 1: Report saved to: /home/mavindu/Desktop/full_zapscan/reports/tab-alawwal-qa-trade-universal.directfn.net_report.html
|▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉| 3/3 [100%] in 9:01.4 (0.00/s) 


-----------| CyberSec v0.1 :: by Mavindu_Wijesekara |-----------
+------------------------------------------------------------------------------+
|       -----------| CyberSec v0.1 :: by Mavindu_Wijesekara |-----------       |
+-----------------------------------------------------+--------+---------------+
| URL                                                 | Status | Title         |
+-----------------------------------------------------+--------+---------------+
| http://tab-ajc-qa-trade-universal.directfn.net      |  200   |               |
| http://tab-alawwal-qa-trade-universal.directfn.net  |  200   |               |
| http://tab-alkahir-dev-trade-universal.directfn.net |  403   | 403 Forbidden |
+-----------------------------------------------------+--------+---------------+







   [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

