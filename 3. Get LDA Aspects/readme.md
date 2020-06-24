This directory contains code used to build an LDA model using some set of articles in a particular event collection.

1. `lda_online_exp_dated.py`: The main file that does the work. It expects inputs that are obtained after running (2) and (3). Finally outputs the LDA model, and related necessary files like dictionary etc.

2. `create_doc_list.ipynb`: Script to create a chronologically ordered list of articles.

2. `preprocess.ipynb`: Preprocess the texts in articles.

Reference: Anirban Sen.