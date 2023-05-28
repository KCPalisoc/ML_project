from sklearn.naive_bayes import MultinomialNB
from Dashboard.load_and_clean.tweet_preprocess import twitter_test
from Dashboard.load_and_clean.yelp_preprocess import yelp_sample_unequal, yelp_sample_equal, \
                                                     hyper_tuning, combo

nb_score, time_lst_nb = hyper_tuning(yelp_sample_equal, 
                                  yelp_sample_unequal, 
                                  MultinomialNB(), 
                                  combo)