# bias-free-news-aggregator
Bias Free News Aggregator

Algorithmically generated news feeds may contain biases in the representation they provide to different temporally evolving aspects of a news event. We address a unique problem in this setting, to generate a daily news-feed that ensures short-term diversity in the aspects of a news event covered in the feed over a window of around two weeks, along with long-term fairness in the representation it provides to these aspects over a window of three months. We additionally build a method so that the algorithm adjusts to how the production of aspects changes over time for the particular news event. We evaluate this over four policy events in India, and show that our algorithm outperforms the baselines in terms of fairness and diversity of apsect representation. Our work is different from most other research on fairness in news recommendation that consider ranking of news items within a single news-feed, since it considers a temporal dimension while ensuring fairness and diversity over different windows of time. Our recommendation framework is easily generalizable to other datasets. A limitation of our work is that we do not consider user-level personalization at this stage.

The code is divided into easy steps that our pipeline follows, and also the different kinds of experimentation that we perform.

For data associated with outputs/libraries/cache used with each file/notebook, find the following link - 
https://drive.google.com/drive/folders/1vbzR_kUD0wn1qGo9Lkg4V5HsJ7xAaFH7?usp=sharing

Please reach out to chakshugoyal97@gmail.com for any issues.
