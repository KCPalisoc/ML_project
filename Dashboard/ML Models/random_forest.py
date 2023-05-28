from sklearn.ensemble import RandomForestClassifier
from Dashboard.load_and_clean.tweet_preprocess import twitter_test
from Dashboard.load_and_clean.yelp_preprocess import yelp_sample_unequal, yelp_sample_equal, \
                                                     hyper_tuning, combo

rf_score, time_lst_rf  = hyper_tuning(yelp_sample_equal, 
                                      yelp_sample_unequal, 
                                      RandomForestClassifier(), 
                                      combo)