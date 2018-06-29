import re
import csv

#book = xlwt.Workbook()
#sheet1 = book.add_sheet("QuestionsFeature")

tagfile = open("tag.txt", "rt")
#questionFile = "benchmark.csv"
questionFile_qald = "benchmark_qald.csv"
#questionFeaturefilename="questionFeature.csv"
questionFeaturefilename_qald="questionFeature_qald.csv"


patternR=re.compile("http:\/\/dbpedia.org\/resource\/[0-9a-zA-Z]\s?")
patternC=re.compile("http:\/\/dbpedia.org\/ontology\/[A-Z]\s?")
patternO=re.compile("http:\/\/dbpedia.org\/ontology\/[a-z]\s?")

tagListG=["_DT ", "_IN ", "_JJ ", "_JJR ", "_JJS ", "_NN ", "_NNS ", "_NNP ", "_NNPS ", "_PRP ", "_RB ", "_RBR ",
         "_RBS ", "_UH ", "_VB ", "_VBD ", "_VBG ", "_VBN ", "_VBP ", "_VBZ ", "_WDT ", "_WP ", "_WP$ ", "_WRB "]

ansTypeList1=["is", "did", "do", "does", "was", "were", "are",
             "Is", "Did", "Do", "Does", "Was", "Were", "Are"]


ansTypeList2=["how many", "How many"]

ansTypeList3=["Count", "count"]

class featureExtractQue:

    def findQuestionLength(self, qstr=""):
        qlen = 0
        tmpList = qstr.split()
        print "qlen: ",len(tmpList) -1
        return (len(tmpList) -1)

    def findNumofTagsList(self, qstr=""):
        tagListno = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, len(tagListG)):
            tagListno[i]=qstr.count(tagListG[i])
        print "tagListG:  ",[tagListG[i]+":"+str(i) for i in range (0, len(tagListG))]
        print "tagListno: ",[str(tagListno[i])+":"+str(i)+"   " for i in range (0, len(tagListno))]
        print tagListno
        return tagListno

    def findNumOftriples(self, qstr=""):
        trpLen= qstr.count("dbpedia.org")
        print "trpLen: ",trpLen
        return trpLen

    def findNumOfRes(self, qstr=""):
        qstrList=qstr.split(",")
        qstr = ' '.join(qstrList)
        resLen = len(re.findall(patternR, qstr))
        print "resLen: ",resLen
        return resLen

    def findNumOfOntoCls(self, qstr=""):
        qstrList=qstr.split(",")
        qstr = ' '.join(qstrList)
        clsLen = len(re.findall(patternC, qstr))
        print "clsLen: ",clsLen
        return clsLen

    def findNumOfOntoO(self, qstr=""):
        qstrList=qstr.split(",")
        qstr = ' '.join(qstrList)
        onLen = len(re.findall(patternO, qstr))
        print "onLen: ",onLen
        return onLen


    def findNoOfAnsTypesList(self, qstr=""):
        ansTypeList=[0, 0, 0]

        if qstr.split()[0] in ansTypeList1:
            ansTypeList[0]=ansTypeList[0]+1
        elif qstr.split()[0]+' '+qstr.split()[1] in ansTypeList2 or qstr.split()[0] in ansTypeList3:
            ansTypeList[1] = ansTypeList[1] + 1
        else:
            ansTypeList[2] = ansTypeList[2] + 1

        print "ansTypeList: ",ansTypeList
        return ansTypeList

    def listToString(self, list):
        return ",".join(str(x) for x in list)


f = featureExtractQue()



feaTCsvFile = open(questionFeaturefilename_qald, 'wt')
csvWriter = csv.writer(feaTCsvFile, quoting=csv.QUOTE_ALL)
csvWriter.writerow(["QuestionID", "Question", "QuestionLength", "TripleSize", "ResourceTotal", "ClassTotal",
                    "RelationTotal","_DT ", "_IN ", "_JJ ", "_JJR ", "_JJS ", "_NN ", "_NNS ", "_NNP ", "_NNPS ", "_PRP ", "_RB ", "_RBR ",
         "_RBS ", "_UH ", "_VB ", "_VBD ", "_VBG ", "_VBN ", "_VBP ", "_VBZ ", "_WDT ", "_WP ", "_WP$ ", "_WRB ", "BooleanAns",
                    "NumberAnswer", "ListAnswer"])
qusFile = open(questionFile_qald, 'r')
tagFile = open('ansPosTag339.txt', 'r')
reader = csv.reader(qusFile)
for row in reader:
    line = ('\t'.join(row)).split("\t")
    print line[1]
    dbList=[]

    qlen = f.findQuestionLength(line[1])
    tagList = f.findNumofTagsList(tagFile.readline())
    tagStr = f.listToString(tagList)
    trpLen = f.findNumOftriples(line[2])
    resLen = f.findNumOfRes(line[2])
    clsLen = f.findNumOfOntoCls(line[2])
    ontLen = f.findNumOfOntoO(line[2])
    ansTypeList = f.findNoOfAnsTypesList(line[1])
    ansTypeStr = f.listToString(ansTypeList)
    dbList.append(resLen)
    dbList.append(clsLen)
    dbList.append(ontLen)
    dbStr = f.listToString(dbList)

    # csvWriter.writerow([line[0], line[1], qlen, trpLen, dbStr, tagStr, ansTypeStr])
    csvWriter.writerow(
        [line[0], line[1], qlen, trpLen, dbList[0], dbList[1], dbList[2], tagList[0], tagList[1], tagList[2],
         tagList[3], tagList[4], tagList[5], tagList[6], tagList[7], tagList[8], tagList[9], tagList[10], tagList[11],
         tagList[12], tagList[13], tagList[14], tagList[15], tagList[16], tagList[17], tagList[18], tagList[19],
         tagList[20],
         tagList[21], tagList[22], tagList[23],
         ansTypeList[0], ansTypeList[1], ansTypeList[2]])


