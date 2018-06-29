import csv
import json

spC = ['@', '$', '-', '%', '&', '*', '#', '!', '^', '?', '+', '(', ')', '~', ':', '{', '}', '.', '_']

def findWords(l):
    p,q = 0,0

    p = l[0].count('_') + 1
    if len(l)>1:
        q = l[1].count('_') + 1

    return p,q

def iSSpecialCharacter(l):
    flag = False
    p = 0
    for sp in spC:
        p = l.count(sp)
        if p > 0 :
            flag = True
            break
    return flag

def isCapital(s1):
    flag = True
    for s in s1.split():
        if(s[0].upper() != s[0]):
            flag = False
            break

    return flag

def checkRelation(uri):
    flag = False
    if '/ontology/' in uri:
        uri = uri.replace('http://dbpedia.org/ontology/', '')
    if '/property/' in uri:
        uri = uri.replace('http://dbpedia.org/property/', '')

    if uri[0].lower() == uri[0]:
        flag = True

    return flag



dict = {}
with open('FullyAnnotated_LCQuAD.json', 'r') as inputfile:
    inputdata = json.loads(inputfile.read())
    for que in range(len(inputdata)):
        labels = []
        for e in range(len(inputdata[que]['predicate mapping'])):
            if (checkRelation(inputdata[que]['predicate mapping'][e]['uri']) == True):
                labels.append(inputdata[que]['predicate mapping'][e]['label'])
        dict[inputdata[que]['question']]= labels
        #print inputdata[que]['question'], labels


l = []
print dict
# ofile  = open('entityEx2.csv', "wb")
# writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
# with open('resources.txt', 'r') as file:
#     for line in file.readlines():
#         #strArray0 = line.rstrip().replace('http://dbpedia.org/resource/', '').split(', ')
#         strArray=[]
#         strArray2 = line.rstrip().replace('http://dbpedia.org/resource/', '').split(', ')
#         for i in range(len(strArray2)):
#             strArray.append(strArray2[i].replace('_', ' '))
#         strArray1 = line.rstrip().split(', ')
#         implicit = 0
#         print strArray
#         print strArray1
#         try:
#             print strArray[0].lower()
#             print dict[strArray1[0]].lower()
#             explicit = (strArray[0].lower() == dict[strArray1[0]].lower())
#             if len(strArray1) > 1:
#                 print strArray[1].lower()
#                 print dict[strArray1[1]].lower()
#                 implicit = (strArray[1].lower() == dict[strArray1[1]].lower())
#
#             #print dict[strArray1[0]], dict[strArray1[1]]
#         except:
#             pass
#         #p,q= findWords(strArray0)
#         #writer.writerow([p, q])
#         writer.writerow([explicit, implicit])
#         l.append(strArray1)
# print l
#
#
#
# print len(dict)

# ofile  = open('entityCS.csv', "wb")
# writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
# with open('resources.txt', 'r') as file:
#     for line in file.readlines():
#         #strArray0 = line.rstrip().replace('http://dbpedia.org/resource/', '').split(', ')
#         strArray=[]
#         strArray2 = line.rstrip().replace('http://dbpedia.org/resource/', '').split(', ')
#         C = [None, None]
#         for i in range(len(strArray2)):
#             strArray.append(strArray2[i].replace('_', ' '))
#         strArray1 = line.rstrip().split(', ')
#         implicit = 0
#         #print strArray
#         print strArray1
#         try:
#             for i in range(len(strArray1)):
#                 print dict[strArray1[i]]
#                 s1 = dict[strArray1[i]].split('_')
#                 C[i]=isCapital(s1)
#
#         except:
#             pass
#         writer.writerow([C[0],C[1]])
#         l.append(strArray1)


# ofile  = open('entityW2.csv', "wb")
# writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
# with open('resources.txt', 'r') as file:
#     for line in file.readlines():
#         strArray0 = line.rstrip().replace('http://dbpedia.org/resource/', '').split(', ')
#         print strArray0
#         C = [None, None]
#
#         for i in range(len(strArray0)):
#             C[i] = iSSpecialCharacter(strArray0[i])
#         print C
#         writer.writerow([C[0],C[1]])
#         l.append(strArray0)


# ofile  = open('entityCapitalSmall.csv', "wb")
# writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
# j = 1
# with open('questions.txt', 'r') as file:
#  for line in file.readlines():
#      str=''
#      for key, value in dict.items():
#          if line.strip() in key:
#              str = key
#              #print str
#              break
#      strArray0 = dict[str]
#      print j, strArray0
#      j = j + 1
#      C = [None, None]
#      for i in range(len(strArray0)):
#          C[i] = isCapital(strArray0[i])
#      #print C
#      writer.writerow([C[0],C[1]])
#      l.append(strArray0)

ofile  = open('labels.csv', "wb")
writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
j = 1
with open('questions.txt', 'r') as file:
  for line in file.readlines():
      str=''
      strArray0=[]
      for key, value in dict.items():
          if line.strip() in key:
              str = key
              #print str
              break
      if (str !=''):
        strArray0 = dict[str]
      print j, strArray0
      j = j + 1
      C = [None, None, None]
      for i in range(len(strArray0)):
          C[i] = strArray0[i]
      #print C
      writer.writerow([C[0],C[1], C[2]])

def isImplict(s1, s2):
    print s1, s2
    if s1 == s2:
        return True
    else:
        return False


# ofile  = open('entityImplicit.csv', "wb")
# writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
# j = 1
# with open('questions.txt', 'r') as fileQ:
#  with open('resources.txt', 'r') as fileR:
#      linesQ = fileQ.readlines()
#      linesR = fileR.readlines()
#      for l in range(len(linesQ)):
#         str=''
#         for key, value in dict.items():
#             if linesQ[l].strip() in key:
#                 str = key
#                       #print str
#                 break
#         rArray = linesR[l].replace('http://dbpedia.org/resource/', '').strip().split(', ')
#         qArray = dict[str]
#         print rArray
#         print qArray
#         strArray0 = []
#         #print j
#         j = j + 1
#         #print len(qArray), len(rArray)
#         for i in range(len(qArray)):
#             strArray0.append(isImplict(rArray[i].lower(), qArray[i].lower().replace(' ', '_')))
#         C = [None, None]
#         for k in range(len(strArray0)):
#             C[k] = strArray0[k]
#          #print C
#         writer.writerow([C[0],C[1]])


