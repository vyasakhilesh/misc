import csv

def noOfwords(str):
    st = str.strip().split()
    return len(st)

print noOfwords("I am the one")

def isExplicit(str1, str2):
    str1 = str1.strip().lower().replace(' ','')
    str2 = str2.split(",")
    for i in range(len(str2)):
        st1 = str2[i].strip().replace("http://dbpedia.org/ontology/", '').lower().replace(' ', '')
        if (str1==st1):
            return 1
    return 0

print isExplicit("new man free", "http://dbpedia.org/ontology/newManFre,http://dbpedia.org/ontology/newManFree")


def isHidden(str):
    if (str.strip() == "@@@"):
        return 1
    return 0

print isHidden("123")


def is500000(value):
    if (value==str(500000)):
        return 1
    return 0

print (is500000(50000))

with open("RelationQ_withoutproperty_FM.tsv", "r") as parseFile:
    ofile = open('Relation_FM.csv', "wb")
    writer = csv.writer(ofile,quoting=csv.QUOTE_ALL)
    parseFile.readline()
    for line in parseFile.readlines():
        sp = line.strip().split("\t")
        print sp
        C = [0, 0, 0, 0, 0, 0, 0, 0]

        C[0] = noOfwords(sp[2])
        C[1] = noOfwords(sp[3])
        C[2] = isExplicit(sp[2], sp[4])
        C[3] = isExplicit(sp[3], sp[4])
        C[4] = isHidden(sp[2])
        C[5] = isHidden(sp[3])
        C[6] = is500000(sp[2])
        C[7] = is500000 (sp[3])
        print C[0], C[1], C[2], C[3], C[4], C[5], C[6], C[7]
        avg = float(sp[5])
        print avg, C[0]+C[1]/avg
        writer.writerow([(C[0]+C[1])/avg, (C[2]+C[3])/avg, (C[4]+C[5])/avg, C[6]+C[7]])





