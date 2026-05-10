#step 1: import the libraries
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# step 2: download 
nltk.download('all')

# step 3: open the text file
file=open('sample.txt','r')
file    

# step 4: read the file
content=file.read()
content

# step 5: use the libraries
sentance=sent_tokenize(content)
sentance

#step 6:
Word=word_tokenize(content)
Word

#step 7:
pos_tags=nltk.pos_tag(Word)
pos_tags

#for costum tokenizer
from nltk.tokenize import RegexpTokenizer
tokenize=RegexpTokenizer(f"\w+")
wor=tokenize.tokenize(content)
wor

# step 8:
pos_tags=nltk.pos_tag(Word)
pos_tags

# step 9:
from nltk.corpus import stopwords

#step 10:
stop_word=set(stopwords.words('english'))
stop_word

# step 11:
filter_word=[word for word in Word if word not in stop_word]
filter_word

# step 12:
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
stemm_word=[stemmer.stem(word) for word in filter_word ]
stemm_word

# step 13:
from nltk.stem import WordNetLemmatizer
lemm=WordNetLemmatizer()
lemm_word=[lemm.lemmatize(word) for word in filter_word]
lemm_word

# step 14:
processed_text=" ".join(lemm_word)
processed_text

#step 15:
from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer()
tf_matrix=vectorizer.fit_transform([processed_text])
print("term",vectorizer.get_feature_names_out())
print(tf_matrix.toarray())

#step 16:
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer()
tfidf_matrix=tfidf.fit_transform([processed_text])
print(tfidf_matrix.toarray())