from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('token.pickle')#File that stores user login data -- make fiel beforehand can just be empty i think
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)# file from google
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '-07:00'      # PDT/MST/GMT-7
EVENT = {
    'summary': 'The Real Test',
    'start':  {'dateTime': '2019-02-13T19:00:00%s' % GMT_OFF},
    'end':    {'dateTime': '2019-02-13T22:00:00%s' % GMT_OFF},
    'location': 'Georgetown University',
    'description': 'This is a very nice test event please come we are desperate!',
    'attendees': [
        {'email': 'test1@email.com'},
        {'email': 'test2@email.com'},
    ],
}

e = GCAL.events().insert(calendarId='3vh66p2d72g0gnv7cl5m06s42o@group.calendar.google.com',
        sendNotifications=True, body=EVENT).execute()

print('''*** %r event added:
    Start: %s
    End:   %s''' % (e['summary'].encode('utf-8'),
        e['start']['dateTime'], e['end']['dateTime']))
