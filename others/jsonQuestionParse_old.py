#!/usr/bin/env python
"""This program execute
   Run:
   $ python JsonQueryParser.py

"""
import sys
import json
import os
import unicodedata
from collections import defaultdict
import csv
import re

dbo = "http://dbpedia.org/ontology/"
res = "http://dbpedia.org/resource/"

pattern=re.compile("dbo:[0-9a-zA-Z]\s?")
pattern1=re.compile("res:[0-9a-zA-Z]\s?")
patternR=re.compile("res:[0-9a-zA-Z]\s?")
patternC=re.compile("dbo:[A-Z]\s?")
patternO=re.compile("dbo:[a-z]\s?")



class QueryDataBase(object):
    def __init__(self, inputfilepath):
        self.inputfilepath = inputfilepath
        self.database=defaultdict(list)

    def openFile(self):
        if os.path.exists(self.inputfilepath):
            with open(self.inputfilepath, 'r') as inputfile:
                try:
                    tmpinputdata = json.loads(inputfile.read())
                    inputfile.close()
                    return tmpinputdata
                except IOError:
                    print "Error :Input file read or open error "
                    sys.exit()
                except TypeError:
                    print "Error :Input file json error "
                    sys.exit()
        else:
            print "Error :File path does not exist"
            sys.exit()


    def createDataBase(self, inputData):
        csvfile = open('questions_qald.csv', 'wt')
        csvfileR = open('questions_qaldR.csv', 'wt')
        csvfileC = open('questions_qaldC.csv', 'wt')
        csvfileO = open('questions_qaldO.csv', 'wt')
        csvWriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvWriterR = csv.writer(csvfileR, quoting=csv.QUOTE_ALL)
        csvWriterC = csv.writer(csvfileC, quoting=csv.QUOTE_ALL)
        csvWriterO = csv.writer(csvfileO, quoting=csv.QUOTE_ALL)
        for id in range (15000, 15000+len(inputData['questions'])):
            if "en" == str(inputData['questions'][id - 15000]["body"][0]["language"]):
                print inputData['questions'][id - 15000]["body"][0]["string"]
                q = inputData['questions'][id - 15000]["body"][0]["string"].replace("?", "").strip()
                q1 = q[:] + " ?"
                # print q1
                q2 = q1.encode('utf-8').strip()
                dbLinks = ""
                if("true" == str(inputData['questions'][id - 15000]["onlydbo"])):
                    if "query" in inputData['questions'][id-15000]:
                        query = inputData['questions'][id-15000]["query"].split()
                        print query
                        queryDB = [s for s in query if(pattern.match(s) or pattern1.match(s))]
                        print queryDB
                        dbLinks = ",".join(queryDB ).replace("dbo:", dbo).replace("res:", res)
                        print dbLinks

                        queryDBR = [s for s in query if (patternR.match(s))]
                        print queryDBR
                        dbLinksR = ",".join(queryDBR).replace("res:", res)
                        print dbLinksR

                        queryDBC = [s for s in query if (patternC.match(s))]
                        print queryDBC
                        dbLinksC = ",".join(queryDBC).replace("dbo:", dbo)
                        print dbLinksC

                        queryDBO = [s for s in query if (patternO.match(s))]
                        print queryDBO
                        dbLinksO = ",".join(queryDBO).replace("dbo:", dbo)
                        print dbLinksO

                        #print queryRES
                        #query = re.sub(r'dbo:\S[a-zA-Z]?', dbo, query)
                        #print q

                        #print q2
                csvWriter.writerow( [id, q2, dbLinks])
                csvWriterR.writerow([id, q2, dbLinksR])
                csvWriterC.writerow([id, q2, dbLinksC])
                csvWriterO.writerow([id, q2, dbLinksO])
                dbLinks=""
                dbLinksR=""
                dbLinksC=""
                dbLinksO=""




def main():

    inputfilepath = "freeformatter-out.json"

    queryDataBase = QueryDataBase(inputfilepath)

    inputData = queryDataBase.openFile()

    queryDataBase.createDataBase(inputData)





if __name__ == "__main__":
    main()
