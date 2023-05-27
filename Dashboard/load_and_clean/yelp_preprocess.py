import pandas as pd

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