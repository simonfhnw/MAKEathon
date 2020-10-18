import logging
import pandas as pd
import numpy as np
from numpy import random
import gensim
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup
from sklearn.linear_model import SGDClassifier
import glob
import pandas as pd
import os

# get data file names
path =r'C:/Development/MAKEathon/text_files'
filenames = glob.glob(path + "/*.txt")

dfs = []
cpes = []
i = 0

for filename in filenames:
    f = open(filename, "r")
    first_line = f.readline()
    lines = f.readlines()[0:]
    full_text = ' '.join(lines)
    full_text = full_text.rstrip("\n")
    first_line = first_line.rstrip("\n")
    dfs.append(full_text)
    cpes.append(first_line)

dict = {'CPE': cpes, 'text': dfs}
df = pd.DataFrame(dict)

# print(df)

df = pd.read_csv('stack-overflow-data.csv')
df = df[pd.notnull(df['tags'])]
print(df.head(10))
print(df['post'].apply(lambda x: len(x.split(' '))).sum())

# split into training and test set
X = df.post
y = df.tags
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)

# model
sgd = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
               ])
sgd.fit(X_train, y_train)

y_pred = sgd.predict(X_test)

print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred,target_names=my_tags))