import json
from datetime import datetime

jsonfile = open('jsonpingpong.json', 'r')
jsondata=jsonfile.read()

events = json.loads(jsondata)

for event in events['events']:
    data = datetime.fromtimestamp(event['startTimestamp']).strftime('%H:%M - %d/%m/%Y')
    stato = event['status']['type']
    casa = event['homeTeam']['name']
    ospite = event['awayTeam']['name']
    if stato == 'notstarted':
        print(f"{casa} vs {ospite}: Inizio alle {data}")
    elif stato == 'inprogress':
        print(f"{casa} vs {ospite}: in corso")
    elif stato == 'canceled':
        print(f"{casa} vs {ospite}: cancellato")
    elif stato == 'finished':
        punti_casa = event['homeScore']['normaltime']
        punti_ospite = event['awayScore']['normaltime']
        print(f"{casa} vs {ospite}: {punti_casa} - {punti_ospite}")