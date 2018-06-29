import sys, getopt
import json
from SPARQLWrapper import SPARQLWrapper, JSON
#from  import

sparql = SPARQLWrapper('http://dbpedia.org/sparql')

#ifile = 'unofficial_update_final_dataset.json'
#ofile = 'questions_answers.json'
#ifile = 'document.json'
#ofile = 'document_answers.json'

ifile = 'qaldquerydarmen.json'
ofile = 'qaldquerydarmen_answer.json'

def generateanswers(ifile, ofile):
    with open(ifile, 'r') as f:
        data = json.load(f)

        output = []
        for i in data:
            #print i['ID']
            #sparql.setQuery(i['sparql_query'])
            for k in range(1,5):
                query = 'Query' + str(k)
                if('SELECT' in i[query] ):
                    answers = []
                    sparql.setQuery(i[query])
                    print i['ID']
                    #try:
                    sparql.setReturnFormat(JSON)
                    results = sparql.query().convert()
                    print results
                    #print results
                    if 'results' in results.keys():
                        #print results['results']['bindings']
                        for result in results['results']['bindings']:
                            if 'uri' in result.keys():
                                answers.append(result['uri']['value'])
                            elif 'callret-0' in result.keys():
                                answers.append(result['callret-0']['value'])
                    elif 'boolean' in results.keys():
                        answers.append(results['boolean'])

                    print answers
                    output.append({'qid': i['ID'],
                                   'qsparql_query': i[query],
                                   'sparql_answers': answers})
                #except:
                    #print "Error", i['ID']


    with open(ofile, 'w') as f:
        json.dump(output, f)

generateanswers(ifile, ofile)
