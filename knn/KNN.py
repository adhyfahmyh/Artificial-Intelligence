import csv
import random
import math
import operator
import pandas as pd

def load(filename, split, trainingset=[], testset=[]):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        dataset = list(reader)
        for x in range (len(dataset)):
            for y in range(5):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split :
                trainingset.append(dataset[x])
            else:
                testset.append(dataset[x])

def load2(trainingset=[], testset=[]):
    with open(r'DataTrain_Tugas3_AI.csv') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            trainingset.append(row)
    with open(r'DataTest_Tugas3_AI.csv') as csvfile:
        reader2 = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader2:
            testset.append(row)

def euclidean(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow(instance1[x] - instance2[x], 2)
    return math.sqrt(distance)

def getNeighbors(trainingset, testinstance, k):
    distances = []
    length = len(testinstance)-1
    for x in range(len(trainingset)):
        dist = euclidean(testinstance, trainingset[x], length)
        distances.append((trainingset[x], dist))
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

def getAccuracy(testset, predictions):
    correct = 0
    for x in range(len(testset)):
        if predictions[x] == testset[x][-1]:
            correct += 1
        akurasi = (correct/float(len(testset))) * 100
    return akurasi

def main():
    trainingset=[]
    testset=[]
    split = 0.67
    load(r'DataTrain_Tugas3_AI.csv',split ,trainingset, testset)
    print ('train set: ' +repr(len(trainingset))+ ' lines')
    print ('test set: ' +repr(len(testset))+ ' lines')
    acc=[]
    prediction = []
    k = 3
    for x in range(len(testset)):
        neighbors = getNeighbors(trainingset, testset[x], k)
        result = getResponse(neighbors)
        prediction.append(result)
        print('X1= '+repr(testset[x][0])+', X2= '+repr(testset[x][1])+', X3= '+repr(testset[x][2])+', X4= '+repr(testset[x][3])+', X5= '+repr(testset[x][4])+', PREDICTED = ' +repr(result)+ ', ACTUAL= ' +repr(testset[x][-1]))
    accuracy = getAccuracy(testset, prediction)
    acc.append(accuracy)
    print("ACCURACY = " +repr(accuracy)+ "%")
    print('_____________________________________________________________________________________________________')
    print('')

def main2():
    trainingset=[]
    testset=[]
    load2(trainingset, testset)
    print ('train set: ' +repr(len(trainingset))+ ' lines')
    print ('test set: ' +repr(len(testset))+ ' lines')
    X1 = []
    X2 = []
    X3 = []
    X4 = []
    X5 = []
    prediction = []
    k = 3
    for x in range(len(testset)):
        neighbors = getNeighbors(trainingset, testset[x], k)
        result = getResponse(neighbors)
        prediction.append(result)
        print('predicted = ' +repr(result))
        X1.append(testset[x][0])
        X2.append(testset[x][1])
        X3.append(testset[x][2])
        X4.append(testset[x][3])
        X5.append(testset[x][4])
    file_name = "TebakanTugas3.csv"
    df = pd.DataFrame([X1, X2, X3, X4, X5, prediction])
    df = df.transpose()
    df.to_csv(file_name, index=False, header=None)

main()
main2()
