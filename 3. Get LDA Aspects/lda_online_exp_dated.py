import pandas as pd
import numpy as np
import pickle
import re
import timeit
import spacy

import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel, HdpModel, LdaModel, LdaMulticore
from nltk.corpus import stopwords
import helper as he
import sys
import datetime as dt
from datetime import datetime


print("Event->")
event = input()

#Load the date to text and text to date mapping
sorted_date_to_text=pickle.load(open('sorted_date_to_text_' + event + '.pkl','rb'))
sorted_text_to_date=pickle.load(open('sorted_text_to_date_' + event + '.pkl','rb'))


def get_optimal_num_topics(corpus,id2word,data):
	'''
	Method to get the maximum coherence model for LDA.
	Input: data_lemmatized (corpus), id2word dictionary
	Returns: optimal model, optimal number of topics
	'''
	max_coherence=-float('inf')
	for num_top in range(5,35):  
		print("topics-> ", num_top)  
		lda_orig = LdaMulticore(corpus, num_topics=num_top, id2word=id2word, workers=7, chunksize=2000, passes=10, batch=False)

		coherencemodel2 = CoherenceModel(model=lda_orig,texts=data,dictionary=id2word,coherence='c_v')

		coherence=coherencemodel2.get_coherence()
		if coherence>max_coherence:
			max_coherence=coherence
			lda=lda_orig
			numtop=num_top
	return(lda,num_top)

def get_docs_for_time_period(start_date,n):
	'''
	Method to return the docs for n months from start_date.
	'''
	if type(start_date)==str:
		start_date=datetime.strptime(start_date,'%Y-%m-%d').date()
	#end_date=(start_date + dt.timedelta(n*365/12))
	end_date=(start_date+dt.timedelta(n*7))
	#Collection of text within the date range
	coll=[]
	for date in sorted_date_to_text.keys():
		date1=datetime.strptime(date,'%Y-%m-%d').date()
		if date1>=start_date and date1<end_date:
			coll.extend(sorted_date_to_text[date])
	return(coll,end_date)
#chunksize=int(sys.argv[1])


print("Loading Data...")
# Load Data - corp.pkl contains data_lemmatized, id2word, corpus
#data_lemmatized is the complete data (list of lists of words)
with open('corp_' + event + '.pkl', 'rb') as f:
	data_lemmatized, id2word, _ = pickle.load(f)


# Number of documents to consider as part of existing model in simulation
start_date=list(sorted_date_to_text.keys())[0]
#The last date in the sorted dictionary (with dates as keys) in string format
last_date=list(sorted_date_to_text.keys())[len(sorted_date_to_text.keys())-1]
#Convert the last date into datetime
last_date=datetime.strptime(last_date,'%Y-%m-%d').date()

####################################################################################################################
#Get the initial corpus on which the original model will be trained
INITIAL_DOCS,end_date = get_docs_for_time_period(start_date, 24)
INITIAL_DOC_SIZE=len(INITIAL_DOCS)
# Set data to contain only first INITIAL_DOC_SIZE documents (initial model to be built on this)
data = data_lemmatized[:INITIAL_DOC_SIZE]
#Build the corpus on initial data
corpus = [id2word.doc2bow(doc) for doc in data]

# Building for the first time - To be considered as the starting/existing model in simulation.
start = timeit.default_timer()

#Get the optimal number of topics using the c_v measure
print("Building Model...")
lda_orig,num_topics=get_optimal_num_topics(corpus, id2word, data)
print("Built the initial model.")

#lda_orig = LdaMulticore(corpus, num_topics=35, id2word=id2word,
#                   workers=3, chunksize=2000, passes=10, batch=False)
end = timeit.default_timer()

time_taken = end - start
print("Initial model trained successfully.")
lda_orig.save( event + '.model')