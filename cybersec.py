#!/usr/bin/python3
import signal
import argparse
import textwrap
import threading
import requests as rq
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from alive_progress import alive_bar
from urllib3.exceptions import InsecureRequestWarning
from zapv2 import ZAPv2
import time
import os

# Exception 
rq.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

API_KEY = 'a70p8l1f5i04pgk6ujhko76dov'
ZAP_URL = 'http://localhost:8080'  # Assuming ZAP is running on localhost
zap = ZAPv2(apikey=API_KEY, proxies={'http': ZAP_URL, 'https': ZAP_URL})
REPORT_DIR = '/home/mavindu/Desktop/full_zapscan/reports'

# Function to display ASCII banner
def display_banner():
    print("---------------------------------------------------------------------------------------------------------------")
    print("------------ | Automate the scan for checking live hosts and vulnerabilities.| --------------")
    print("---------------------------------------------------------------------------------------------------------------")
    print(" /  __ \\     | |             /  ___|          ")
    print("| /  \\/_   _| |__   ___ _ __\\ `--.  ___  ___ ")
    print("| |   | | | | '_ \\ / _ \\ '__|`--. \\/ _ \\/ __|")
    print("| \\__/\\ |_| | |_) |  __/ |  /\\__/ /  __/ (__ ")
    print(" \\____/\\__, |_.__/ \\___|_|  \\____/ \\___|\\___|")
    print("        __/ |                                ")
    print("       |___/                                 ")
    print("                                      V 0.1")
    print("        ---------------------|by Mavindu_Wijesekara")
    print("-------------------------------------------------------------")

# Get arguments
parser = argparse.ArgumentParser(
    prog='CyberSec.py',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
-------------------------------------------------------------
------------ | Mass scan for checking live hosts | --------------
-------------------------------------------------------------'''),
    usage='python3 %(prog)s -u [URLList] -to [Timeout]',
    epilog='---------------- Script from YourWebsite.com ----------------')

parser._action_groups.pop()
required = parser.add_argument_group('[!] Required arguments')
required.add_argument('-u', '--urllist', metavar='', required=True, help='Target URLs file')
required.add_argument('-to', '--timeout', metavar='', type=int, help='Set timeout (Default is 3)')
args = parser.parse_args()

# Style
class style():
    HEADER = '\033[95m'
    BLINK = '\33[5m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BOLD  = '\033[1m'
    RESET = '\033[0m'
    RED = '\033[31m'

# Get URL list
with open(args.urllist) as f:
    url_list = [x.rstrip() for x in f]

# Set Timeout
if args.timeout is not None:
    t_out = args.timeout
else:
    t_out = 3

# Table Settings
table = PrettyTable()
table.title = "-----------| CyberSec v0.1 :: by Mavindu_Wijesekara |-----------"
table.field_names = ['URL', 'Status', 'Title']
table.align['URL'] = 'l'
table.align['Title'] = 'l'
table.sortby = 'Status'

def quit(signal, frame):
    print (style.RED+"----------| Program stopped due to CTRL + C "+style.RESET)
    print("Bye!")
    raise SystemExit

def add_default_scheme(url):
    """ Add http:// if no scheme is present """
    if not url.startswith(('http://', 'https://')):
        return 'http://' + url
    return url

# Function to scan the URL using ZAP and generate a report
def zap_scan(url):
    print(f"Starting ZAP scan for {url}")
    # Start new session for each URL
    session_name = "session_" + str(int(time.time()))
    zap.core.new_session(name=session_name, overwrite=True)

    # Spider Scan
    print(f"Starting spider scan on: {url}")
    scan_id = zap.spider.scan(url)
    while int(zap.spider.status(scan_id)) < 100:
        print(f"Spider scan progress: {zap.spider.status(scan_id)}%")
        time.sleep(5)
    print("Spider scan completed")

    # Active Scan
    print(f"Starting active scan on: {url}")
    scan_id = zap.ascan.scan(url)
    while int(zap.ascan.status(scan_id)) < 100:
        print(f"Active scan progress: {zap.ascan.status(scan_id)}%")
        time.sleep(5)
    print("Active scan completed")

    # Generate and save the report
    report_name = os.path.join(REPORT_DIR, f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}_report.html")
    print(f"Generating report for {url} at {report_name}")
    with open(report_name, 'w') as report_file:
        report_file.write(zap.core.htmlreport())
    print(f"Report saved to: {report_name}")

# Function to check live URLs and then scan them using ZAP
def run():
   with alive_bar(len(url_list), bar='blocks') as bar:
      for url in url_list:
         try:
            url = add_default_scheme(url)  # Add scheme if missing
            req = rq.get(url, timeout=t_out, verify=False)
            soup = BeautifulSoup(req.text, 'html.parser')
            if soup.title is not None:
               table.add_row([url, req.status_code, soup.title.text])
            else:
               table.add_row([url, req.status_code, 'Title Not Found'])

            # If URL is live, perform the ZAP scan
            if req.status_code == 200:
                zap_scan(url)

            bar()
         except rq.exceptions.ConnectionError as errc:
            print(style.RED+"[!] Error Connecting: Check your internet connection!!"+style.RESET)
         except rq.exceptions.Timeout as errt:
            print(style.YELLOW+"[!] Timeout Error: Max timeout reached"+style.RESET)
         except rq.exceptions.RequestException as err:
            print(style.RED+"[!] OOps: Something Else: ", str(err)+style.RESET)
            raise SystemExit
   print("\n\n-----------| CyberSec v0.1 :: by Mavindu_Wijesekara |-----------")
   print(table)
   print("\n\n")
   raise SystemExit

# Main
if __name__ == '__main__':
   signal.signal(signal.SIGINT, quit)
   
   # Display banner before running the scan
   display_banner()

   run_thread = threading.Thread(target=run)
   run_thread.start()

