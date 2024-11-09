#!/usr/bin/env python3
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timezone, timedelta
import pytz

SERVICE_ACCOUNT_FILE = 'secrets.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/calendar.readonly']
)

service = build('calendar', 'v3', credentials=credentials)
calendar_id = 'crashspacela@gmail.com'

local_tz = pytz.timezone('America/Los_Angeles')
now = datetime.now(local_tz)
time_min = (now - timedelta(minutes=20)).isoformat()
time_max = (now + timedelta(minutes=20)).isoformat()

events_result = service.events().list(
    calendarId=calendar_id,
    timeMin=time_min,
    timeMax=time_max,
    singleEvents=True
).execute()

events = events_result.get('items', [])
if events:
    print(f'<h1>{events[0]["summary"]}</h1>\n<p>{events[0]["description"]}</p><hr>')

