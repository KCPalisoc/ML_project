import pandas as pd
from itertools import product
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
import time

yelp_sample_unequal = pd.read_csv('Dashboard/Data/yelp_reviews_35_000.csv')

yelp_sample_unequal['length'] = yelp_sample_unequal['text'].apply(len)
yelp_sample_unequal['stars'] = yelp_sample_unequal['stars'].astype(float)

yelp_classify = yelp_sample_unequal.loc[:, ['stars', 'text']]

x_unequal = yelp_classify['text']
y_unequal = yelp_classify['stars']

unequal_count = y_unequal.value_counts()
min_count = unequal_count.min()
yelp_sample_equal = (yelp_sample_unequal.groupby('stars').apply(lambda x: x[:min_count]))
equal_count = yelp_sample_equal['stars'].value_counts()

x_equal = yelp_sample_equal['text']
y_equal = yelp_sample_equal['stars']

combo = list(product(('all_stars', '1_5_stars', '1_3_5_stars'), 
                     ('unigram', 'bigram', 'trigram'), 
                     ('equal','unequal')))

def star_df(star, df):
    """
    This function takes in a string of star classification and subsets the 
    rows of the data for the corressponding stars
    """
    
    if 'all_stars' == star:
        return  df
    elif '1_5_stars' == star:
        return df[(df['stars']==1) | (df['stars']==5)]
    else:
        return df[(df['stars']==1) | (df['stars']==3) | (df['stars']==5)]
    
def n_gram_df(str, df):
    """
    This function takes in a string for the corresponding n-gram and the 
    subsetted star data frame. Then creates the ngram and then creates a 
    Spacy Sparce data matrix.
    """
    
    x_df = df['text']
    if str == 'unigram':
        unigram_vocab = (CountVectorizer(ngram_range=(1,1), stop_words='english')
                         .fit(df.loc[:, 'text']))
        return unigram_vocab.transform(x_df)
        
    elif str == 'bigram':
        bigram_vocab = (CountVectorizer(ngram_range = (2, 2), stop_words='english')
                        .fit(df.loc[:, 'text']))
        return bigram_vocab.transform(x_df)
    else: 
        trigram_vocab = (CountVectorizer(ngram_range = (3, 3), stop_words='english')
                         .fit(df.loc[:, 'text']))
        return trigram_vocab.transform(x_df)
    
def model_to_acuracy(model,x_train, x_test, y_train, y_test, combo):
    """
    This function takes in the train and test data each variation, 
    visualizes, calculates model prediction, and returns accuracy score as a numpy int.
    """

    model.fit(x_train, y_train)
    predmnb = model.predict(x_test)
    y = pd.concat([y_train, y_test])

    #accuracy score only for even data
    if y.value_counts().nunique() == 1:

        score = round(accuracy_score(y_test, predmnb) * 100, 2)
        print(combo, "Accuracy Score:", score)
        print()

    #f1 for uneven data 
    else:
        score = round(f1_score(y_test, predmnb, average='weighted') * 100, 2)
        print(combo, "f1_score:", score)
        print()

    return score

def hyper_tuning(yelp_sample_equal, yelp_sample_unequal, model, hyper_combo):
    """
    This function calculates the accuracy score for each variation of 
    hyperpermeters for a given model
    """

    score_lst = []
    time_lst = []
    
    for tup in hyper_combo:
        
        star, gram, equal = tup

        if equal == 'equal':

            yelp_classify_equal = yelp_sample_equal.loc[:, ['stars', 'text']]
            star_class_df = star_df(star, yelp_classify_equal)
            x_df = n_gram_df(gram, star_class_df)
        else: 
            yelp_classify_unequal = yelp_sample_unequal.loc[:, ['stars', 'text']]
            star_class_df = star_df(star, yelp_classify_unequal)
            x_df = n_gram_df(gram, star_class_df)

        y_df = star_class_df['stars']

        (x_train, x_test, y_train, y_test) = train_test_split(x_df, 
                                                 y_df, 
                                                 test_size=0.2, 
                                                 random_state=101)
        start_time = time.time()
        score = model_to_acuracy(model,x_train, x_test, y_train, y_test, tup)
        end_time = time.time()
        score_lst.append(score)
        time_lst.append((float(end_time) - float(start_time))/float(60))

    return score_lst, time_lst