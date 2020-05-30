import os
import pandas as pd
import numpy as np

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

import sys
import re
from time import time

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
import pickle
import warnings
warnings.filterwarnings('ignore')

from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer


def data_preprocess(root, lemmatizer_flag=True):
    '''
    Data preprocess
    :param root (str): root directory
    :return data, label (pd series): data and label
    '''
    data = []
    label = []
    # read file
    for folder in os.listdir(root):
        if folder != '.DS_Store':
            path = root + '/' + folder
            for file in os.listdir(path):
                # append the folder name as labels
                label.append(folder)
                f = open(path + '/' +file)
                content = f.read()
                if lemmatizer_flag:
                    data.append(lemmatize_sentence(content))
                else:
                    content = re.findall("[\w']+", content)
                    # filter the valid words and append to data
                    data.append(content2String(content))
                
    return pd.Series(data), pd.Series(label)


def content2String(lis): 
    '''
    Content list to string
    :param lis (list): content list
    :return: filterd content string
    '''
    # initialization
    str1 = ""  
    alphabet = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for ch in lis: str1 += ch + " "
    return ''.join(filter(alphabet.__contains__, str1)) 


def get_wordnet_pos(treebank_tag):
    '''
    Data preprocess
    :param treebank_tag:
    :return wordnet: 
    '''
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def lemmatize_sentence(sentence):
    '''
    Data preprocess
    :param sentence (str): input text 
    :return str: lemmatized test string
    '''
    res = []
    lemmatizer = WordNetLemmatizer()
    for word, pos in pos_tag(word_tokenize(sentence)):
        wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        res.append(lemmatizer.lemmatize(word, pos=wordnet_pos))

    return ' '.join(res)


def run_predic(data):
    
    model = pickle.load(open('model.pkl', 'rb'))
    X_test, y_test = data_preprocess(data)
    pred = model.predict(X_test)
    report = metrics.classification_report(y_test, pred,target_names=y_test.unique(), output_dict=True)
    
    return ("Classification report %s:\n%s\n" % (model, report))

