import csv
import json

spC = ['@', '$', '-', '%', '&', '*', '#', '!', '^', '?', '+', '(', ')', '~', ':', '{', '}', '.','0', '1','2'
       '3','4','5','6','7','8','9']

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
    for s in s1:
        if(s[0].upper() != s[0]):
            flag = False
            break

    return flag

dict = {}
with open('jerrl_ent.json', 'r') as inputfile:
    inputdata = json.loads(inputfile.read())
    for que in range(len(inputdata)):
        for e in range(len(inputdata[que]['entity mapping'])):
            dict[inputdata[que]['entity mapping'][e]['uri']]=inputdata[que]['entity mapping'][e]['label']


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





