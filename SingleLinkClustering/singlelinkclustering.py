import math
import csv
import sys
import numpy
K_MAX = 10
ID = 0
DISTANCE_MAX = sys.float_info.max


'''example convert 0 1 0 0 0 0 0 0 0 0 to 2'''
def convertBitToDigit(list):
    for i in range(0, len(list)):
        if(list[i]!=0):
            return i

    return None

'''inst1 = [1,1,0,1], inst2 = [0,0,1,0] euclideanDistance = 2.0'''
def euclideanDistance(instance1, instance2):
    #print instance1, instance2
    length = len(instance1)
    distance = 0.0
    for i in range(length):
        distance += pow((instance1[i] - instance2[i]), 2)
    return math.sqrt(distance)

'''0.1 0.0 0.0 0.0 ..... 0 1 0 0 0 0 0 0 0 0 ' to [[0.1 0.0 0.0 0.0.....], 2, id]'''
def convertStringtoFilterlist(tmpStr):
    global ID
    tmplist = tmpStr.rstrip().split(" ")
    clusterWithNum = [[]]
    tmpListNum = []
    length = len(tmplist)
    for i in range(0, len(tmplist)):
        if i < (length - 10):
            clusterWithNum[0].append(float(tmplist[i]))
        else:
            tmpListNum.append(int(tmplist[i]))
    clusterWithNum.append(convertBitToDigit(tmpListNum))
    clusterWithNum.append(ID)
    ID = ID + 1
    return clusterWithNum


#Using SingleLink distance
def findClosestPair(cluster1, cluster2):
    distance = DISTANCE_MAX

    #print cluster1, cluster2
    for i in range(0, len(cluster1)):
        for j in range(0, len(cluster2)):
            tmpDistance = euclideanDistance(cluster1[i][0], cluster2[j][0])
            if (tmpDistance <= distance):
                distance = tmpDistance
    #print distance
    return round(distance, 2)




def agglomerativeClustering(clusterDataset):
    for k in range(0, K_MAX ):
        closestPair = ()
        distance = DISTANCE_MAX
        if(len(clusterDataset) >= 2):
            for i in range(0, len(clusterDataset)):
                for j in range(i + 1, len(clusterDataset)):
                    tmpDistance = findClosestPair(clusterDataset[i], clusterDataset[j])
                    #print (tmpDistance, distance)
                    if(tmpDistance <= distance):
                        distance = tmpDistance
                        closestPair = (i, j)
            #print closestPair
            for x in range(len(clusterDataset[closestPair[1]])):
                clusterDataset[closestPair[0]].append(clusterDataset[closestPair[1]][x])
            clusterDataset.remove(clusterDataset[closestPair[1]])

        #print clusterDataset
    return clusterDataset




def parsingFile(fileName):
    clusterDataset = []
    with open(fileName, 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            clusterDataset.append([convertStringtoFilterlist(dataset[x][0])])
    return clusterDataset


def main():

    clusterDataset = parsingFile("semeion.data")
    clusterDatasetforK = agglomerativeClustering(clusterDataset)

    l = [[[[2],9, 0],[[4],1, 1]],[[[7],2, 2]],[[[10],4, 3]], [[[11],4, 4]], [[[11.5],9, 5]], [[[10],4, 6]], [[[12.5],9, 7], [[13],4, 8]]]
    #clusterDatasetforK =  agglomerativeClustering(l)

    for i in range(len(clusterDatasetforK)):
        print "Cluster-"+str(i) + ":{",
        for j in range(len(clusterDatasetforK[i])):
            print str(clusterDatasetforK[i][j][2])+ ",",
        print "}, ",


    row, column = len(clusterDatasetforK), 10
    confusionMatrix = [[0 for x in range(column)] for y in range(row)]
    for i in range(len(clusterDatasetforK)):
        for j in range(10):
            confusionMatrix[i][j]=0

    for i in range(len(clusterDatasetforK)):
        for j in range(len(clusterDatasetforK[i])):
             k = clusterDatasetforK[i][j][1]
             confusionMatrix[i][k] += 1

    print "{"+"\t0\t"+"1\t"+"2\t"+"3\t"+"4\t"+"5\t"+"6\t"+"7\t"+"8\t"+"9\t"+"}"
    for i in range(len(clusterDatasetforK)):
        print "M"+str(i)+":{",
        for j in range(10):
            print str(confusionMatrix[i][j]),
        print "}"



if __name__ == "__main__":
    main()
