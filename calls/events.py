from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

def getallevents(service):
        try:
        # Call the Calendar API
            print('Getting the upcoming 10 events')
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                                singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('No upcoming events found.')
                return

        # Prints the start and name of the next 10 events
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])

        except HttpError as error:
            ('An error occurred: %s' % error)


def getTodaysEvents(service):
    try:
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                                timeMax=now,
                                                singleEvents=True,
                                                orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get(
                    'dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
            ('An error occurred: %s' % error)



def getNEvents(service,nEvents):
    try:
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              timeMax=now, maxResults=nEvents,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get(
                'dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        ('An error occurred: %s' % error)

#####Testing#####