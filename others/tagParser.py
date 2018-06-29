import operator
import xlwt
import sys
import os

book = xlwt.Workbook()
sheet1 = book.add_sheet("TagQuestions")

file = open("tag.txt", "r")

dictTag = {}

for line in file:
    l= line.split("\t", 1)
    #print l[0], l[1].rstrip()
    key = str(l[0])
    disc = str(l[1].rstrip())
    value = []
    value.append(disc)
    value.append(0)
    dictTag[key]=value
#print dictTag
tags = ["_"+key for key in dictTag]
print tags

fileTag=open("sample1.txt", "rw")
queFile = open("question.txt", "r")

id = 0
'''for que in queFile:
    row = sheet1.row(id)
    #print type(que.rstrip())
    row.write(0, que.rstrip().decode('utf-8'))
    id = id+1'''

''' = 0
for que in fileTag:
    row = sheet1.row(id)
    #print type(que.rstrip())
    row.write(1, que.rstrip().decode('utf-8'))
    id = id+1'''

queFile = open("question.txt", "r")
for que in queFile:
    fileTag = open("sample1.txt", "r+")
    print que
    fileTag.write(que.decode('utf-8'))
    fileTag.close()
    os.system("./stanford-postagger.sh models/english-left3words-distsim.tagger sample1.txt > ans.txt")
    ansFile = open("ans.txt", "r")
    lines = ansFile.readlines()
    print lines[1].rstrip()
    ansFile.close()

'''id = 0
for line in ansFile:
    tmpDictTag = dictTag
    for tag in tags:
        count = line.count(tag+" ")
        tmpDictTag[tag[1:]][1]= count
    sorted_x = sorted(tmpDictTag.items(), key=operator.itemgetter(0))
    print sorted_x
    #sorted_x = sorted(tmpDictTag.items(), key = lambda x: x[0])
    #row = sheet1.row(id)
    #row.write(1, sorted_x)
    id = id + 1'''

id = 0
for line in fileTag:
    tmpDictTag = dictTag
    for tag in tags:
        count = line.count(tag+" ")
        tmpDictTag[tag[1:]][1]= count
    sorted_x = sorted(tmpDictTag.items(), key=operator.itemgetter(0))
    print sorted_x
    #sorted_x = sorted(tmpDictTag.items(), key = lambda x: x[0])
    row = sheet1.row(id)
    row.write(0, line.decode('utf-8'))
    i = 0
    #print sorted_x[0][1][1]
    for item in sorted_x:
        row.write(i+1, sorted_x[i][1][1])
        i = i+1
    id = id + 1

book.save("tag_parse_Question.xlsx")
    #tmpDictTag1 = {K:V for K, V in tmpDictTag.iteritems() if(V[1] != 0)}
    #print tmpDictTag1
