#!/usr/bin/env python
"""This program execute
   Run:
   $ python JsonQueryParser.py

"""
import sys
import json
import os
import xlwt
import csv

from collections import defaultdict

pattern = "http://dbpedia.org/ontology"
excelFile = "datasetQuestion.xlsx"
csvFile="questions.csv"
questionId = 10000



class QueryDataBase(object):
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("dataset")
    cols = ["A", "B", "C"]
    txt = [0, 1, 2]

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
        global questionId
        print len(inputData)
        csvfile = open('questions.csv', 'wt')
        csvWriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for id in range (10000, 10000+len(inputData)):
            #questionId = questionId + 1
            self.writeDataToexcel(id-10000, id, inputData[id-10000]["corrected_question"], inputData[id-10000]["sparql_query"])
            q = inputData[id-10000]["corrected_question"].replace("?", "").strip()
            print q
            q1= q[:]+" ?"
            print q1
            q2 = q1.encode('utf-8').strip()
            print q2
            csvWriter.writerow([id, q2])

        self.book.save("datasetQuestion.xlsx")


    def writeDataToexcel(self, id, questionId, question, query):
        print ""
        row = self.sheet1.row(id)
        row.write(0, str(questionId))
        row.write(1, question)
        row.write(2, query)



def main():

    inputfilepath = "unofficial_update_final_dataset.json"

    queryDataBase = QueryDataBase(inputfilepath)

    inputData = queryDataBase.openFile()

    queryDataBase.createDataBase(inputData)

   # print(queryDataBase.wb.get_sheet_names())



if __name__ == "__main__":
    main()
