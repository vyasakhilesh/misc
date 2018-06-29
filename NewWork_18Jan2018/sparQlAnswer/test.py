import json

file = ''
with open(file, 'r') as f:
    data = json.load(f)
    output = []
    for i in data:
        q1 = i['Query']
        sp = q1.split('|\\')
        print i['ID'], len(sp), sp