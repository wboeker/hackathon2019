from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from facebook import *

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('token.pickle')#File that stores user login data -- make file beforehand can just be empty i think
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)# file from google
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

#currently looping from 0-5 (6 times)
for x in range(0, len(events_Array)):
    EVENT = {
        'summary': events_Array[x]['name'],
        'start':  {'dateTime': events_Array[x]['start_time']},
        'end':    {'dateTime': events_Array[x]['end_time']},
        'location': events_Array[x]['place']['name'],
        'description': events_Array[x]['description'],
    }

    e = GCAL.events().insert(calendarId='3vh66p2d72g0gnv7cl5m06s42o@group.calendar.google.com',
        sendNotifications=True, body=EVENT).execute()

    print('''*** %r event added:
        Start: %s
        End:   %s''' % (e['summary'].encode('utf-8'),
            e['start']['dateTime'], e['end']['dateTime']))