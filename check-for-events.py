#!/usr/bin/env python3
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timezone, timedelta
import pytz

service = build('calendar', 'v3', 
                credentials = service_account.Credentials.from_service_account_file('secrets.json', scopes=['https://www.googleapis.com/auth/calendar.readonly']))

now = datetime.now(pytz.timezone('America/Los_Angeles'))

events_result = service.events().list(
    calendarId='crashspacela@gmail.com',
    timeMin=(now - timedelta(minutes=20)).isoformat(),
    timeMax=(now + timedelta(minutes=20)).isoformat(),
    singleEvents=True
).execute()

events = events_result.get('items', [])
if events:
    print(f'<h1>{events[0]["summary"]}</h1>\n<p>{events[0]["description"]}</p><hr>')
