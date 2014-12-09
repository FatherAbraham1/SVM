from sklearn import svm
from sklearn.metrics import confusion_matrix
import os
import sys
import random
import pylab as pl 
import time
files = ["data/svmguide1.txt", "data/mushroom.txt", "data/rcv1_train.binary.txt","data/covtype.txt"]
for filename in files:
    start = time.clock()
    start2 = time.time()
    df = open(filename,'r')
    print "done loading file "+ filename

    data = df.read().split('\n')
    ##random.shuffle(data)
    col = len(data)*2/3
    print col
    train_data=data
    test_data = data[col:]

    labels=[]
    features=[]
    for entry in train_data:
    	tmp =entry.split(' ')
    	labels.append(tmp[0])
    	feature=[]
    	for tmp2 in tmp[1:]:
    		feature.append(tmp2)
    	features.append(feature)

    test_labels=[]
    test_features=[]
    for entry in test_data:
    	tmp =entry.split(' ')
    	test_labels.append(tmp[0])
    	feature=[]
    	for tmp2 in tmp[1:]:
    		feature.append(tmp2)
    	test_features.append(feature)
    clf = svm.SVC()
    clf.fit(features, labels)
    end = time.clock()
    end2= time.time()
    print "training process time is "+ str(end-start)
    print "training wall time is "+ str(end2-start2)

    start = end
    start2 = end2
    
    preds = clf.predict(test_features)
    #print preds
    # Compute confusion matrix
    cm = confusion_matrix(test_labels, preds)
    
    print(cm)
    zeros = cm[0]

    ones = cm[1]
    accuracy1 = (zeros[0]+ones[1])*1.0/len(test_labels)
    print "accuracy is " + str(accuracy1)
    end = time.clock()
    end2= time.time()
    print "process time is "+ str(end-start)
    print "wall time is "+ str(end2-start2)