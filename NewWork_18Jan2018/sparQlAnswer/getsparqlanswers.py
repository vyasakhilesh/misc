import sys, getopt
import json
from SPARQLWrapper import SPARQLWrapper, JSON
#from  import

sparql = SPARQLWrapper('http://dbpedia.org/sparql')

#ifile = 'unofficial_update_final_dataset.json'
#ofile = 'questions_answers.json'
#ifile = 'document.json'
#ofile = 'document_answers.json'


def generateanswers(ifile, ofile):
    with open(ifile, 'r') as f:
        data = json.load(f)

        output = []
        for i in data:
            answers = []
            #print i['ID']
            #sparql.setQuery(i['sparql_query'])
            sparql.setQuery(i['Query1'])
            try:
                sparql.setReturnFormat(JSON)
                results = sparql.query().convert()
                #print results
                if 'results' in results.keys():
                    #print results['results']['bindings']
                    for result in results['results']['bindings']:
                        if 'v0' in result.keys():
                            answers.append(result['v0']['value'])
                        elif 'callret-0' in result.keys():
                            answers.append(result['callret-0']['value'])
                elif 'boolean' in results.keys():
                    answers.append(results['boolean'])

                '''output.append({'_id': i['_id'],
                               'question': i['corrected_question'],
                               'sparql_query': i['sparql_query'],
                               'sparql_answers': answers})'''
                output.append({'qid': i['ID'],
                               'qsparql_query': i['query'],
                               'sparql_answers': answers})
            except:
                print "Error", i['ID']


    with open(ofile, 'w') as f:
        json.dump(output, f)

generateanswers(ifile, ofile)

'''def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,'hi:o:',['ifile=','ofile='])
    except getopt.GetoptError:
        print('getsparqlanswers.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('getsparqlanswers.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-o', '--ofile'):
            outputfile = arg
    generateanswers(inputfile, outputfile)


if __name__ == '__main__':
    main(sys.argv[1:])'''