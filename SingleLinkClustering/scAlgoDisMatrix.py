import math
import csv
import sys
K_MAX = 10
ID = 0
DISTANCE_MAX = sys.float_info.max
dataListGlobal = []
distanceMatrixGlobal = []

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

'''Matrix to store distance between all instances'''
def euclideanDistanceMatrix():
    global dataListGlobal
    global distanceMatrixGlobal
    row, column = len(dataListGlobal), len(dataListGlobal)
    #print row, column
    distanceMatrixGlobal = [[0 for x in range(column)] for y in range(row)]
    for i in range(row):
        for j in range(column):
            if(i == j):
                distanceMatrixGlobal[i][j] = DISTANCE_MAX
            else:
                distanceMatrixGlobal[i][j]= euclideanDistance(dataListGlobal[i], dataListGlobal[j])


'''0.1 0.0 0.0 0.0 ..... 0 1 0 0 0 0 0 0 0 0 ' to [0.1 0.0 0.0 0.0.....], [id, 2]'''
def convertStringtoFilterlist(tmpStr):
    global ID
    tmplist = tmpStr.rstrip().split(" ")
    clusterWithNum = []
    tmpListNum = []
    dataList = []
    for i in range(0, (len(tmplist) - 10)):
        dataList.append(float(tmplist[i]))

    for i in range(0, 1):
        clusterWithNum.append(ID)

    for j in range(-10, 0):
        tmpListNum.append(int(tmplist[j]))

    clusterWithNum.append(convertBitToDigit(tmpListNum))

    ID = ID+1
    return dataList, clusterWithNum


#Using SingleLink distance
def findClosestPair(cluster1, cluster2):
    global dataListGlobal
    global distanceMatrixGlobal
    distance = DISTANCE_MAX
    #print cluster1, cluster2
    for i in range(0, len(cluster1)):
        for j in range(0, len(cluster2)):
            x, y = cluster1[i][0], cluster2[j][0]
            tmpDistance = distanceMatrixGlobal[x][y]
            #tmpDistance = 0.0
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
            '''Merger Cluster'''
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
        dataListFull = []
        for x in range(len(dataset)):
            #print dataset[x][0]
            dataList, num  = convertStringtoFilterlist(dataset[x][0])
            clusterDataset.append([num])
            dataListFull.append(dataList)
    #print dataListFull
    return dataListFull, clusterDataset


def main():
    global dataListGlobal
    dataListFull, clusterDataset = parsingFile("semeion.data")
    dataListGlobal = dataListFull
    euclideanDistanceMatrix()
    clusterDatasetforK = agglomerativeClustering(clusterDataset)

    '''for i in range(len(distanceMatrixGlobal)):
        for j in range(len(distanceMatrixGlobal[i])):
            print distanceMatrixGlobal[i][j],'''

    '''Print ClusterdataSet'''
    for i in range(len(clusterDatasetforK)):
        print "Cluster-"+str(i) + ":{",
        for j in range(len(clusterDatasetforK[i])):
            print str(clusterDatasetforK[i][j][0])+ ",",
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

    '''Print ConfusionMatrix'''
    #print "{"+"\t0\t"+"1\t"+"2\t"+"3\t"+"4\t"+"5\t"+"6\t"+"7\t"+"8\t"+"9\t"+"}"
    for i in range(len(clusterDatasetforK)):
        print "M"+str(i)+":{",
        for j in range(10):
            print str(confusionMatrix[i][j]),
        print "}"



if __name__ == "__main__":
    main()
