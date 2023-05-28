from sklearn.linear_model import LogisticRegression
from Dashboard.load_and_clean.tweet_preprocess import twitter_test
from Dashboard.load_and_clean.yelp_preprocess import yelp_sample_unequal, \
                                                     yelp_sample_equal, \
                                                     hyper_tuning, combo

var_holder = {}
max_iter_list = [100,1000,10000] 

for iter in max_iter_list:
    print("Number of Iterations: ", iter)
    (var_holder['lr_acc_' + str(iter)], 
     var_holder['time_lst_' + str(iter)]) = hyper_tuning(yelp_sample_equal, 
                                                         yelp_sample_unequal, 
                                                         LogisticRegression(max_iter=iter), 
                                                         combo)