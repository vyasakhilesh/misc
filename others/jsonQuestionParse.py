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

pattern2=re.compile("<http:\/\/dbpedia.org\/resource\/[0-9a-zA-Z]\s?")
pattern=re.compile("dbo:[0-9a-zA-Z]\s?")
pattern1=re.compile("res:[0-9a-zA-Z]\s?")
patternR=re.compile("res:[0-9a-zA-Z]\s?")
patternC=re.compile("dbo:[A-Z]\s?")
patternO=re.compile("dbo:[a-z]\s?")



class QueryDataBase(object):
    def __init__(self, inputfilepath):
        self.inputfilepath = inputfilepath
        self.database=defaultdict(list)

    def listToString(self, list):
        return ",".join(str(x) for x in list)

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
        csvfileRA = open('questions_qaldRA.csv', 'wt')
        csvfileCA = open('questions_qaldCA.csv', 'wt')
        csvfileOA = open('questions_qaldOA.csv', 'wt')
        csvWriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvWriterR = csv.writer(csvfileR, quoting=csv.QUOTE_ALL)
        csvWriterC = csv.writer(csvfileC, quoting=csv.QUOTE_ALL)
        csvWriterO = csv.writer(csvfileO, quoting=csv.QUOTE_ALL)
        csvWriterRA = csv.writer(csvfileRA, quoting=csv.QUOTE_ALL)
        csvWriterCA = csv.writer(csvfileCA, quoting=csv.QUOTE_ALL)
        csvWriterOA = csv.writer(csvfileOA, quoting=csv.QUOTE_ALL)
        for id in range (15000, 15000+len(inputData['question'])):
            #print inputData['question'][id - 15000]["string"][0]
            #if "@lang" in str(inputData['question'][id - 15000]["string"][0]):
                #print "If-----------------------------------------------------------------------------------------------------------------"
            #    if ("en" == str(inputData['question'][id - 15000]["string"][0]["@lang"])):
                if "#text" in inputData['question'][id - 15000]["string"]:
                    print inputData['question'][id - 15000]["string"]["#text"]
                    q = inputData['question'][id - 15000]["string"]["#text"].replace("?", "").strip()
                else:
                    print inputData['question'][id - 15000]["string"][0]["#text"]
                    q = inputData['question'][id - 15000]["string"][0]["#text"].replace("?", "").strip()

                q1 = q[:] + " ?"
                    # print q1
                q2 = q1.encode('utf-8').strip()
                    #print "If1-----------------------------------------------------------------------------------------------------------------"
                if("true" == str(inputData['question'][id - 15000]["@onlydbo"])):
                    if "query" in inputData['question'][id-15000]:
                        query = inputData['question'][id-15000]["query"].split()
                    else:
                        query = inputData['question'][id - 15000]["pseudoquery"].split()
                        print query
                    queryDB = [s for s in query if(pattern.match(s) or pattern1.match(s) or pattern2.match(s))]
                    dbLinks = ",".join(queryDB ).replace("dbo:", dbo).replace("res:", res)
                    queryDBR = [s for s in query if (patternR.match(s) or pattern2.match(s))]
                    dbLinksR = ",".join(queryDBR).replace("res:", res)
                    queryDBC = [s for s in query if (patternC.match(s))]
                    dbLinksC = ",".join(queryDBC).replace("dbo:", dbo)
                    queryDBO = [s for s in query if (patternO.match(s))]
                    dbLinksO = ",".join(queryDBO).replace("dbo:", dbo)



                    answer = inputData['question'][id - 15000]['answers']
                    print answer
                    if "answer" in inputData['question'][id - 15000]['answers']:
                        #csvWriter.writerow([id, q2, inputData['question'][id - 15000]['answers']["answer"]])
                        csvWriter.writerow([id, q2, dbLinks])
                    else:
                        #csvWriter.writerow([id, q2, self.listToString(answer)])
                        csvWriter.writerow([id, q2, dbLinks])
                    # csvWriterR.writerow([id, q2, dbLinksR, self.listToString(answer)])
                    # csvWriterC.writerow([id, q2, dbLinksC, self.listToString(answer)])
                    # csvWriterO.writerow([id, q2, dbLinksO, self.listToString(answer)])
                    # csvWriterRA.writerow([id, self.listToString(answer)])
                    # csvWriterCA.writerow([id, self.listToString(answer)])
                    # csvWriterOA.writerow([id, self.listToString(answer)])



def main():

    inputfilepath = "freeformatter-out.json"
    #inputfilepath = "qald-6-train-multilingual.json"

    queryDataBase = QueryDataBase(inputfilepath)

    inputData = queryDataBase.openFile()

    queryDataBase.createDataBase(inputData)





if __name__ == "__main__":
    main()
