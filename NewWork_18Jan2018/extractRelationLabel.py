import json
import csv
from collections import OrderedDict
dictQue=OrderedDict()

spC = ['@', '$', '-', '%', '&', '*', '#', '!', '^', '?', '+', '(', ')', '~', ':', '{', '}', '.','0', '1','2'
       '3','4','5','6','7','8','9']

def iSSpecialCharacter(l):
    flag = False
    p = 0
    for sp in spC:
        p = l.count(sp)
        if p > 0 :
            flag = True
            break
    return flag

def isCapital(s):
    flag1 = None
    flag2 = None
    if (len(s)>=1):
        flag1 = True
        s1 = s[0]
        for s3 in s1.split():
            try:
                if(s3[0].upper() != s3[0]):
                    flag1 = False
                    break
            except:
                pass

    if (len(s) >1):
        flag2 = True
        s2 = s[1]
        for s4 in s2.split():
            try:
                if(s4[0].upper() != s4[0]):
                    flag2 = False
                    break
            except:
                pass

    return flag1,flag2


def isImplicit(s, r):
    flag1 = None
    flag2 = None
    rl = r.split(", http://")
    for i in range(len(rl)):
        rl[i] = rl[i].replace('dbpedia.org/resource/', '')
        rl[i] = rl[i].replace('http://', '')
        rl[i] = rl[i].replace('_', ' ')

    print rl , s
    if(len(rl) > 1 and len(s) >1):
        if (rl[1].lower()==s[1].lower()):
            flag2 = True
        else:
            flag2 = False

    if (len(rl) >= 1 and len(s) >= 1):
        if (rl[0].lower() == s[0].lower()):
            flag1 = True
        else:
            flag1 = False

    return flag1,flag2


def isRelation(ent):
    if 'http://dbpedia.org/property/' in ent['uri']:
        return True
    label = ent['uri'].replace('http://dbpedia.org/ontology/', '')
    if label.lower()[0]==label[0]:
        return True
    return False

with open('FullyAnnotated_LCQuAD5000.json') as jsonfile:
     questions = json.loads(jsonfile.read())
     for que in questions:
         tmpLabel = []
         tmpUri = []
         tmp =[]
         for ent in que["predicate mapping"]:
                if isRelation(ent):
                    if 'label' in ent :
                        tmpLabel.append(ent['label'])
                        tmpUri.append(ent['uri'])
                    else:
                        tmpLabel.append('')
                        tmpUri.append(ent['uri'])
         ques = que["question"].replace("?","").strip()
         tmp.append(tmpLabel)
         tmp.append(tmpUri)
         dictQue[ques]= tmp

#print len(dictQue)
#print dictQue
updatedQueDict = OrderedDict()

with open('questions.txt') as qfile:
        questions = qfile.readlines()
        #print len(questions)
        i = 0
        for k, que in enumerate(questions):
            que =  que.strip()
            try:
                if que in updatedQueDict.keys():
                    updatedQueDict[que+'----']=dictQue[que]
                else:
                    updatedQueDict[que]=dictQue[que]
            except:
                #print k+1,que
                if (i==0):
                    #updatedQueDict.append(
                    #("Give me the count of artist in the company whose Artist is Jean", ['Jean - Francois Cote']))
                    updatedQueDict['Give me the count of artist in the company whose Artist is Jean']=[['artist','artist'],['http://dbpedia.org/property/artist','http://dbpedia.org/property/artist']]
                    i = i+1
                else:
                    #updatedQueDict.append(
                        #("Where is the mouth of the river whose tributary is Bjelimi", ['Bjelimicka Rijeka']))
                    updatedQueDict["Where is the mouth of the river whose tributary is Bjelimi"]=[['tributary','mouth'],['http://dbpedia.org/ontology/rightTributary','http://dbpedia.org/ontology/mouthCountry']]
#updatedQueDict.append("Which planet was discovered by Johann Gottfired and Urbain Le Verrier", [])

print len(updatedQueDict)
#print updatedQueDict

import pandas as pd

df = pd.DataFrame()
for key,value in updatedQueDict.items():
    try:
        a = value[0][0]
    except:
        a = ''
    try:
        b = value[0][1]
    except:
        b = ''
    try:
        c = value[1][0]
    except:
        c = ''
    try:
        d = value[1][1]
    except:
        d = ''
    df = df.append(pd.DataFrame({'Questions':key, 'label1':a, 'label2':b , 'uri1':c, 'uri2':d}, index=[0]))

def wordLen(word):
    return len(word.split())

def splitWord(word):
    wordL = []
    for w in list(word):
        if w.upper()== w :
           wordL.append(' '+w.lower())
        else:
           wordL.append(w)
    return wordL




#print df.head(5)
#wordLen
df1 = df[['label1','label2']].applymap(wordLen)
df1.columns = ['label1len', 'label2len']
#print (df1.head(2))
dfR = pd.concat([df, df1], axis=1)
#print dfR.info()
#print dfR.head(2)
#implicitExplicit
dfR['uri1Label'] = dfR['uri1'].str.replace('http://dbpedia.org/ontology/', '').str.replace('http://dbpedia.org/property/', '')
#dfR['uri3Label'] = dfR['uri1Label'].str.replace('http://dbpedia.org/property/', '')
dfR['uri2Label']= dfR['uri2'].str.replace('http://dbpedia.org/ontology/', '').str.replace('http://dbpedia.org/property/', '')
#dfR['uri4Label'] = dfR['uri2Label'].str.replace('http://dbpedia.org/property/', '')
dfR[:] = dfR.loc[['uri1Label', 'uri2Label']].applymap(splitWord)

print dfR.info()
print dfR.head(20)
dfR.to_csv('relationSep2018.csv',index=False)

'''def capsAndExpilcit():
    ofile  = open('cap_implicit.csv', "wb")
    writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
    with open('resources.txt', 'r') as file:
        lines = file.readlines()
        for i in range(len(updatedQueDict)):
            capEnt1, capEnt2 = isCapital(updatedQueDict[i][1])
            print i
            print lines[i].strip(), updatedQueDict[i][1]
            print "Capital:", capEnt1, capEnt2
            implicitEnt1, implicitEnt2 = isImplicit(updatedQueDict[i][1], lines[i].strip())
            print "Explicit:", implicitEnt1, implicitEnt2
            i = i+1
            writer.writerow([capEnt1, capEnt2, implicitEnt1, implicitEnt2])


def specialChar():
    ofile = open('special_12jun2018.csv', "wb")
    writer = csv.writer(ofile, quoting=csv.QUOTE_ALL)
    with open('resources.txt', 'r') as file:
        lines = file.readlines()
        for i in range(len(updatedQueDict)):
            specEnt1 = None
            specEnt2 = None
            print updatedQueDict[i]
            if len(updatedQueDict[i][1])>=1:
                specEnt1 = iSSpecialCharacter(updatedQueDict[i][1][0])
            if len(updatedQueDict[i][1])>1:
                specEnt2 = iSSpecialCharacter(updatedQueDict[i][1][1])
            print "Special:", specEnt1, specEnt2
            i = i + 1
            writer.writerow([specEnt1, specEnt2])

#specialChar()

def totalWord(label):
    return len(label.split())

def wordCount():
    ofile = open('wordCount_12jun2018.csv', "wb")
    writer = csv.writer(ofile, quoting=csv.QUOTE_ALL)
    with open('resources.txt', 'r') as file:
        lines = file.readlines()
        for i in range(len(updatedQueDict)):
            wordEnt1 = None
            wordEnt2 = None
            l1=0
            l2=0
            print updatedQueDict[i]
            if len(updatedQueDict[i][1]) >= 1:
                wordEnt1 = totalWord(updatedQueDict[i][1][0])
            if len(updatedQueDict[i][1]) > 1:
                wordEnt2 = totalWord(updatedQueDict[i][1][1])
            print "Words:", wordEnt1, wordEnt2
            i = i + 1
            if (wordEnt1 !=None and  wordEnt2==None) or wordEnt1 !=None:
                l1 = wordEnt1
            if wordEnt1 !=None and  wordEnt2!=None:
                l2 = (wordEnt1+wordEnt2)/2.0
            print (l1,l2)
            writer.writerow([l1, l2])

wordCount()'''
