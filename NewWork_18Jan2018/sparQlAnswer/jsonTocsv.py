import sys, getopt
import csv
import json


inputfile='document_answers.json'
outputfile='document_answers.csv'
def json2csv(ifile, ofile):
    with open(ifile, 'r') as f:
        data = json.load(f)
        i = 10000

        f = csv.writer(open(ofile, 'wb+'))

        # Write CSV header

        for question in data:
            C = [None for i in range(250)]

            for i in range(len(question['sparql_answers'])):
                if (i < 250):
                    C[i]=question['sparql_answers'][i].encode('utf-8')
                else:
                    break

            ap = []
            ap.append(question['qid'])
            ap.append(question['qsparql_query'].encode('utf-8'))
            for i in C:
                ap.append(i)

            f.writerow(ap)



json2csv(inputfile, outputfile)
