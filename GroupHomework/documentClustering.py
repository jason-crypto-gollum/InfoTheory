# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:47:36 2019

@author: jackl
"""

#with open('test.csv','r') as f:
#    line = f.readline()
#    lines = f.readlines()
#    r = ""
#    for line in lines:
#        line.replace('\n',' ')
#        r += line
#    rr = r.split(',')
#    for r in rr:
#        print(r)
#        print("")
#        print("")

import csv
#'AAAI-14 Accepted Papers.csv'

import re
from math import log

def removePunctuation(text):
    '''
        INPUT:
            text: a string
        remove punctuation in text
        
        OUTPUT: a string
        
    '''
    punctuation = '!,;:?"\'.'
    text = re.sub(r'[{}]+'.format(punctuation),'',text)
    return text.strip().lower()

def loadDataSet():
    '''
        load data from given .csv file
        OUTPUT:
            dataSet: 
                i-th paper is represented as dataSet[i], 
                which consists of all words from title, keyword,abstract in i-th paper
    '''
    dataSet = []
    with open('AAAI-14 Accepted Papers.csv') as f:
        items = csv.reader(f)
        next(items)# skip header
        wordVector = []
        for item in items:
            t = item[0]+" "+item[3]+" "+item[5]# title,keyword, abstract
            t = removePunctuation(t).split()
            dataSet.append(t)
            wordVector += t
       
    return dataSet,list(set(wordVector))

def dfCount(dataSet,wv):
    '''
        document frequency based on a specified word
        df[i] means the frequence of documents which have the i-th word in wordVector wv
        
        OUTPUT:
            df: a vector
    '''
    df = [0]*len(wv)
    for i in range(0,len(wv)):
        for doc in dataSet:
          #  print(wv)
            if wv[i] in doc:
                df[i] += 1
    df = [v/len(dataSet) for v in df]
    return df

def tfCount(dataSet,wv):
    '''
        tf[i] means frequence of word in wv in the i-th doc in dataSet
        tf[i][j] means frequence of j-th word in wv in the i-th doc in dataSet
    '''
    tf = []
    for doc in dataSet:
        tf.append([doc.count(word)/len(doc) for word in wv])
    
    return tf

def tf_idfCalc(tf,df):
    '''
    OUTPUT:
        tf_idf[i][j] means importance of j-th word in i-th document
    
    '''
    tf_idf = []
    for i in range(0,len(tf)):
        tf_idf.append([tf[i][j]*log(1/df[j]) for j in range(0,len(df))])
    
    return tf_idf
        
    
dataSet,wordVector = loadDataSet()
tf = tfCount(dataSet,wordVector)
df = dfCount(dataSet,wordVector)

tf_idf = tf_idfCalc(tf,df)
