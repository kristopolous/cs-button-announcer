#!/usr/bin/env python3
import requests
import os
import sys
import subprocess

status_file = ".last-crash-space-status.txt"

response = requests.get( "https://crashspacela.com/sign/")
if response.status_code == 200:
    page_text = response.text.lower()
    last_status = current_status = "unknown"

    if "open" in page_text:
        current_status = "open"
    elif "closed" in page_text:
        current_status = "closed"
    
    if os.path.exists(status_file):
        with open(status_file, 'r') as file:
            last_status = file.read().strip()
    
    if current_status != last_status:
        open(status_file, 'w').write(current_status)

        if current_status == "open":
            response = os.popen('./animal-say | /usr/bin/msmtp crash-space-open-status@googlegroups.com').read()
            if response:
                print("Error sending email:", response)
        
else:
    print("Failed to retrieve the webpage.")

