import auth.tokencaller
from auth.tokencaller import auth
from calls.events import getTodaysEvents,getallevents
from calls.calendarlist import getCalendarLists
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def main():
    creds=auth()
    service= build('calendar', 'v3', credentials=creds)
    getCalendarLists(service)
    print(getTodaysEvents(service))
    print(getallevents(service))


main()
