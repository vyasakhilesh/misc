import json
import csv

ofile = open('qald5_2018.csv', 'wt')
writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
id = 1
with open("qald5_2018.json", 'r') as file:
    data = json.load(file)
    for que in data['question']:
        for strg in que['string']:
            if(strg['@lang']=='en'):
                text = strg['#text']
                break
        if('query' in que):
            query = que['query']
        else:
            query = que['pseudoquery']

        answers = []
        if(type(que['answers']) is list):
            for ans in que['answers']:
                answers.append(ans)
        else:
            answers.append(que['answers']['answer'])
        print ("id: ", id)
        print ("question: ",text)
        print ("query: ",query)
        print ("Answers: ", answers)
        writer.writerow([id, text, query, str(answers)])
        id = id+1
