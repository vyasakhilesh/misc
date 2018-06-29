import csv
import json

spC = ['@', '$', '-', '%', '&', '*', '#', '!', '^', '?', '+', '(', ')', '~', ':', '{', '}', '.', '_']



def iSSpecialCharacter(l):
    flag = False
    p = 0
    for sp in spC:
        p = l.count(sp)
        if p > 0 :
            flag = True
            break
    return flag


def isExplicit(str1, str2):
    str1 = str1.strip().lower().replace(' ','')
    st1 = str2.strip().replace("http://dbpedia.org/ontology/", '').lower().replace(' ', '')
    if (str1==st1):
        return 1
    return 0

def noOfwords(str):
    st = str.strip().split()
    return len(st)

def checkClass(uri):
    flag = False
    if '/ontology/' in uri:
        uri = uri.replace('http://dbpedia.org/ontology/', '')

    if uri[0].upper() == uri[0]:
        flag = True

    return flag


print checkClass("http://dbpedia.org/ontology/Comic")

dictLabel = {}
dictUri = {}
questEx = {}
with open('FullyAnnotated_LCQuAD.json', 'r') as inputfile:
    inputdata = json.loads(inputfile.read())
    for que in range(len(inputdata)):
        labels = []
        uris = []
        exp = []
        for e in range(len(inputdata[que]['predicate mapping'])):
            if (checkClass(inputdata[que]['predicate mapping'][e]['uri']) == True):
                labels.append(inputdata[que]['predicate mapping'][e]['label'])
                uris.append(inputdata[que]['predicate mapping'][e]['uri'])
                exp.append(isExplicit(inputdata[que]['predicate mapping'][e]['label'], inputdata[que]['predicate mapping'][e]['uri']))
        dictLabel[inputdata[que]['question']]= labels
        dictUri[inputdata[que]['question']]= uris
        questEx[inputdata[que]['question']]= exp
        #print inputdata[que]['question'], labels'''


print dictLabel
print dictUri
print questEx


ofile  = open('classLabelName.csv', "wb")
writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
j = 0
m = []
with open('questions.txt', 'r') as file:
  for line in file.readlines():
      flag = False
      value = []
      for key, valueT in dictLabel.items():
          if line.strip()[0:-5].lower() in key.lower():
              flag = True
              value = valueT

          else:
              pass
              #print line.strip()[0:30].lower(),key
      C = [0, 0, 0, 0, 0, 0, 0, 0]
      j = j+1
      if (flag ==True):
          for i in range(len(value)):
              C[i] = value[i]
      else:
          #print j
          #print line
          m.append(j)

      writer.writerow([C[0], C[1], C[2]])
print len(m)




ofile  = open('classUri.csv', "wb")
writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
j = 0
m = []
with open('questions.txt', 'r') as file:
  for line in file.readlines():
      flag = False
      value = []
      for key, valueT in dictUri.items():
          if line.strip()[0:-5].lower() in key.lower():
              flag = True
              value = valueT

          else:
              pass
              # print line.strip()[0:30].lower(),key
      j = j + 1
      C = [0, 0, 0, 0, 0, 0, 0, 0]
      if (flag == True):
          for i in range(len(value)):
              C[i] = value[i]
      else:
          #print j
          m.append(j)

      writer.writerow([C[0], C[1], C[2]])
print len(m)

j=0
m=[]
ofile  = open('classEX.csv', "wb")
writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
with open('questions.txt', 'r') as file:
      for line in file.readlines():
          flag = False
          value = []
          for key, valueT in questEx.items():
              if line.strip()[0:-5].lower() in key.lower():
                  flag = True
                  value = valueT

              else:
                  pass
                  # print line.strip()[0:30].lower(),key
          C = [0, 0, 0, 0, 0, 0, 0, 0]
          j = j + 1
          if (flag == True):
              for i in range(len(value)):
                  C[i] = value[i]
          else:
              #print j
              m.append(j)

          writer.writerow([C[0], C[1], C[2]])
print len(m)
print m