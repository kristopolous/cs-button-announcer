#!/usr/bin/env python3
import requests
import os
import sys
import subprocess

# URL of the webpage to monitor
url = "https://crashspacela.com/sign/"
# File to store the last known status
status_file = "/home/chris/cs-check/.last-crash-space-status.txt"

email_list = ['crash-space-open-status@googlegroups.com']

# Function to send an email notification using msmtp
def send_email(who):
    recipient = who
    # Create the email content
    # Send the email directly using msmtp
    with os.popen(f'/home/chris/cs-check/animal-say | /usr/bin/msmtp {recipient}') as stream:
        response = stream.read()  # You can check the response if necessary
    if response:
        print("Error sending email:", response)

# Function to check the webpage status
def check_status():
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the page content for the specific text
        page_text = response.text.lower()
        if "open" in page_text:
            current_status = "open"
        elif "closed" in page_text:
            current_status = "closed"
        else:
            current_status = "unknown"
        
        # Read the last known status from the file
        if os.path.exists(status_file):
            with open(status_file, 'r') as file:
                last_status = file.read().strip()
        else:
            last_status = "unknown"
        
        # If the status has changed, send an email and update the file
        if current_status != last_status:

            # Update the status file with the new status
            with open(status_file, 'w') as file:
                file.write(current_status)

            if current_status == "open":
                for email in email_list:
                    send_email(email)
            
    else:
        print("Failed to retrieve the webpage.")

# Run the check
check_status()

