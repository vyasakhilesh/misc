import csv
import numpy as np
import math
import operator

def euclideanDistance(instance1, instance2, length):
    distance = 0.0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

def cosineDistance(instance1, instance2, length):
    den1 = 0.0
    den2 = 0.0
    num  = 0.0
    for x in range(length):
        num += (instance1[x]*instance2[x])
        den1 += pow(instance1[x],2)
        den2 += pow(instance2[x], 2)
    #print (num, den1, den2)
    return (1- num/(math.sqrt(den1*den2)))


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = cosineDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0

def calculateMean(attribute, meanValue):
    #print (attribute)
    meanValue.append(np.mean(attribute))


def calculateStandardDeviation(attribute, standardDevValue):
    #print (attribute)
    standardDevValue.append(np.std(attribute))


def normalizeAttributesInTrainingSet(trainSet, meanValue, standardDevValue):
    for y in range(57):
        #print (len(trainSet))
        for x in range(len(trainSet)):
            #print (trainSet[x][y], meanValue[y], standardDevValue[y] )
            trainSet[x][y] = ((trainSet[x][y] - meanValue[y])/standardDevValue[y])
           # print (trainSet[x][y])

def normaliseTrainingset(trainingSet, meanValue, standardDevValue):
    for y in range(57):
       array = []
       for x in range(len(trainingSet)):
          array.append(trainingSet[x][y])
       calculateMean(array, meanValue)
       calculateStandardDeviation(array, standardDevValue)

    #print (meanValue)
    #print (standardDevValue)
    normalizeAttributesInTrainingSet(trainingSet, meanValue, standardDevValue)

def main():
    # prepare data
    trainingSet = []
    testSet = []
    meanValue = []
    standardDevValue = []

    with open('spam_training.csv', 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(57):  #size of attributes
                dataset[x][y] = float(dataset[x][y])
                #print (dataset[x])
            trainingSet.append(dataset[x])
                #print (trainingSet)
    #print (trainingSet)
    normaliseTrainingset(trainingSet, meanValue, standardDevValue)
    #print(trainingSet)

    with open('spam_test.csv', 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(57): #size of attributes
                dataset[x][y] = float(dataset[x][y])
            testSet.append(dataset[x])

    # generate predictions
    predictions = []
    k = 1 # number of neighbour for prediction
    i = 0
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        i = i + 1
        print(i, '>>>>>>>>> predictedValue=' + repr(result) + ',>>>>>>>>>>> actualValue=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')


main()
