# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:43:15 2019

@author: Axsteen
"""
import pandas as pd
import numpy as np
import urllib
import nltk
nltk.download('punkt')
import bs4 as bs
from nltk.corpus import stopwords
nltk.download('stopwords')

# getting the data source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Citizenship_(Amendment)_Act,_2019').read()

# Parsing the Data / Creating Beautifulsoup object
soup = bs.BeautifulSoup(source,'lxml')

# Fetching the data
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

# preprocessing the data
import re
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

# Preparing the dataset

Sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in Sentences]

type(sentences)
ss = pd.DataFrame(sentences)
ss.to_csv()

