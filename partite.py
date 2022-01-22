import json

jsonfile = open('partita.json', 'r')
jsondata=jsonfile.read()

obj = json.loads(jsondata)

casa = str(obj['homeTeam']['name'])
ospite = str(obj['awayTeam']['name'])

print(casa, 'vs', ospite)