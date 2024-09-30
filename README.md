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
![image](https://github.com/user-attachments/assets/a4b39e0d-83fb-485d-b1a4-527e8fd99e56)



## TEST RUN

![image](https://github.com/user-attachments/assets/771bfb30-c419-4ad1-b186-76595f7c49cc)



   [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

