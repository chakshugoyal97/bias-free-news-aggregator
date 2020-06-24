This directory contains the code associated with performing user studies. Also, provides an example of running the algorithm on custom data and producing news-feeds for consumption.

1. `input-data`: It is sourced from outside [credits: Ankur Sharma & Navreet Kaur], contains some articles belonging to Aadhar & Demonetisation which are labelled as Pro- or Anti-Estabilishment. 
`data.pkl` is a refined version of the raw data `aadhar.pkl` & `demon.pkl`, which have been added for reference.

2. `Refine Data.ipynb`: Takes the raw data and refines it, suitable for input into the recommendation system code.

3. `Generate Feeds.ipynb`: Recommendation System that iteratively outputs feed with varying user preference.

4. `output-feeds`: Contains feeds produced for last 15 days of the timeline run on. The index `i.txt` represents $i * 20%$ user preference for Anti-Estabilishment.