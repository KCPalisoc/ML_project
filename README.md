# Understanding Public Perceptions of the ObamaCare Program: A Sentiment Analysis Approach Utilizing Open-Source Data
A Capstone project for the CAPP 30254 – Machine Learning for Public Policy course where a sentiment analysis of the Affordable Care Act was conducted to analyze public perceptions with five different models: Multinomial Naive Bayes, Decision Tree Classifier, Random Forest Classifier, Logistic Regression, and Neural Networks.

| Most Frequent Negative @'s | Most Frequent Postive @'s |
|----------------------------|---------------------------|
| ![neg @](https://github.com/KCPalisoc/ML_project/blob/main/Dashboard/Graphs/ats.png?raw=true) | ![pos @](https://github.com/KCPalisoc/ML_project/blob/main/Dashboard/Graphs/pos_at.png?raw=true)|

| Most Frequent Negative Hashtags | Most Frequent Postive Hashtags |
|----------------------------|---------------------------|
| ![neg hash](https://github.com/KCPalisoc/ML_project/blob/main/Dashboard/Graphs/hashtags.png?raw=true) | ![pos hash](https://github.com/KCPalisoc/ML_project/blob/main/Dashboard/Graphs/pos_hash.png?raw=true)|


## Project Abstract
Public policy analysts often encounter classification tasks in which there is a scarcity of labeled data to train their models. In the realm of sentiment analysis, however, there exist resourceful approaches to leverage large and publicly available datasets to train models for this purpose. In this study, our objective is to ascertain the prevailing opinion climate concerning one of the most widely discussed government programs in recent years: the Patient Protection and Affordable Care Act (PPACA), commonly referred to as ObamaCare. To achieve this goal, we will develop a customized model using open-source data (i.e. Yelp), to analyze sentiments expressed in tweets related to the ObamaCare program.

## Instructions to execute project codes
NOTE: All codes to be run from within the project root directory

1. Clone this repo
2. From within project root directory ML_project run **poetry install** (takes ~2 minutes for all packages to install)
Activate the virtual environment through **poetry shell**
3. Download these datasets to run the final Jupyter notebooks:
  * Yelp Academic Dataset (https://www.yelp.com/dataset)
  * Twitter Dataset (Private)
4. Navigate from the root directory ML_project -> 'Final Reports'. There, you will find multiple Jupyter notebooks with that contains sentiment classification and analysis for both Yelp reviews and tweets.
