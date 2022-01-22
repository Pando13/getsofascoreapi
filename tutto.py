import json

jsonfile = open('jsonpingpong.json', 'r')
jsondata=jsonfile.read()

obj = json.loads(jsondata)

bho = str(obj['events'])

print(bho)