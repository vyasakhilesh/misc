import csv

fileWhqald="whQueFeaQald.csv"
fileWh3253="whQueFea3253.csv"
questionFile_qald="question339.txt"
questionFile_3253="question_3253.txt"


whList=['Who ','How ', 'In which ', 'What ', 'When ', 'Where ', 'Which ']
whFre=[0, 0, 0, 0, 0, 0, 0]
columns = list(whList)
columns.insert(0, 'Questions')

def calculateWhList(question, l):
    for i in range(0, len(whList)):
        if whList[i] in question[0:12]:
            l[i]=1
            break
    return l

feaTCsvFile = open(fileWhqald, 'wt')
csvWriter = csv.writer(feaTCsvFile, quoting=csv.QUOTE_ALL)
csvWriter.writerow(columns)
qusFile = open(questionFile_qald, 'rt')
for question in qusFile:
    ls = calculateWhList(question, list(whFre))
    tmpFre=list(ls)
    print tmpFre
    tmpFre.insert(0, question.rstrip('\n'))
    csvWriter.writerow(tmpFre)
