from sklearn.tree import DecisionTreeClassifier
from Dashboard.load_and_clean.tweet_preprocess import twitter_test
from Dashboard.load_and_clean.yelp_preprocess import yelp_sample_unequal, yelp_sample_equal, \
                                                     hyper_tuning, combo

dt_score, time_lst_dt = hyper_tuning(yelp_sample_equal,
                                     yelp_sample_unequal, 
                                     DecisionTreeClassifier(), 
                                     combo)