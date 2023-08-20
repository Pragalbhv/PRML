#import block
import os
import numpy as np
import heapq
#______________
import pickle

from utility import *

with open('Vocab.pickle', 'rb') as fa:#loading vocab
    vocabu=pickle.load(fa)
#______________________________________________    
freq_words = heapq.nlargest(2500, vocabu, key=vocabu.get)
def convbow(emails):
    X = []
    for emailidx in range(len(emails)):
        email=emails[emailidx]
        vector = []
        for word in freq_words:
            if word in email:
                vector.append(1)
            else:
                vector.append(0)
        X.append(vector)
    X = np.asarray(X)
    return X
#_________________________________________________
def predict():
    with open('model_pkl' , 'rb') as f:
        svm = pickle.load(f)
    x_test = get_data_list('test/')
    print(svm.predict(convbow(process(cleanmail(x_test)))))
    with open("output.txt", "w") as output:#writing to file
        output.write(str(svm.predict(convbow(process(cleanmail(x_test))))))
        

#_____________________________________________________
predict()