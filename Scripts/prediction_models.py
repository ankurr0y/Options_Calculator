import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.metrics import r2_score

def modelmax(date,high):
    count=[]
    i=0
    #print(type(high))
    for i in range(len(date)):
        count.append(i)
    #print(count)
    #print(len(high))
    '''maximum=0
    for highest in high:
        if highest>maximum:
            maximum=int(highest)'''
    split=int(0.8*len(count))
    train_count=count[:split]
    train_high=high[:split]
    test_count=count[split:]
    test_high=high[split:]
    degree=2
    while True:
        mymodel=np.poly1d(np.polyfit(train_count,train_high,degree))
        r1=r2_score(train_high,mymodel(train_count))
        r2=r2_score(test_high,mymodel(test_count))
        if r1>0.85:
            if r2>0.85:
                #print(r1)
                #print(r2)
                break
            else:
                degree+=1
        else:
            degree+=1
    #print(mymodel)
    model_test=[]
    for j in range(len(test_count)-1):
        model_test.append(mymodel(test_count[j]))
    return max(model_test)

def modelmin(date,low):
    count=[]
    i=0
    for i in range(len(date)-1):
        count.append(i)
    '''maximum=0
    for highest in low:
        if highest>maximum:
            maximum=int(highest)'''
    split=int(0.8*len(count))
    train_count=count[:split]
    train_low=low[:split]
    test_count=count[split:]
    test_low=low[split:]
    degree=2
    while True:
        mymodel=np.poly1d(np.polyfit(train_count,train_low,degree))
        r1=r2_score(train_low, mymodel(train_count))
        r2=r2_score(test_low, mymodel(test_count))
        if r1>0.85:
            if r2>0.85:
                #print(r1)
                #print(r2)
                break
            else:
                degree+=1
        else:
            degree+=1
    #print(mymodel)
    model_test=[]
    for j in range(len(test_count)):
        model_test.append(mymodel(test_count[j]))
    return min(model_test)
