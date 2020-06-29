This directory contains the code associated with comparing Google Alerts vs Mass Media. It contains -

`MA vs GA.ipynb`: This file performs the following analysis (MA stands for Mass Media, GA stands for Google Alerts) - 

1. Eventwise Inventory Comparison - Compare the total corpus we have for Google Alerts and Mass Media for the coverage of four events.

2. Aspectwise Inventory Comparison - For each event, compare how differently do the 2 corpus cover various aspects.

3. Recommendation Algorithms: Fairness, Diversity & Recency - Compare how do MA algorithms (from simulation performed in `4. Recommendation Algorithm`) namely i. "random sampling", ii. "latest picking", iii. "our fairness-diversity heuristic" fare with respect to Google Alerts' recommendation system and each other.

4. Repetition - Check the degree of repetition by different algorithms. Repetition-at-k means what is the probability of an article to be repeated k times. Repetition-at-k for k=0 would mean the probability an article does not gets to be picked by the algorithm, k=1 would mean only once, and so on...
