import json

ifile = 'qald-5_train.json'
ofile = 'qald5_anwer.json'
quefile = 'question339.txt'
dict={}

with open(ifile, 'r') as f:
    data = json.load(f)
    for i in data['questions']:
        dict[i['body'][0]['string']] = i['answers']


print dict
que = open(quefile, 'r')
lines = que.readlines()
output = []
i = 15000
for q in lines:
    q1 = q.strip()[0:-5].lower()
    for que, ans in dict.iteritems():  # for name, age in list.items():  (for Python 3.x)
        if q1 in que.lower():
            output.append({'qid': i,
                               'qsparqll_query': q,
                               'sparql_answers': ans})
    i = i + 1


with open(ofile, 'w') as f:
    json.dump(output, f)