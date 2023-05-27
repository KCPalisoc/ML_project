import pandas as pd
import json

yelp_data = pd.read_json('../Downloads/yelp_data/yelp_academic_dataset_review.json', 
                         lines=True, chunksize=100_000)
for chunk in yelp_data:
    yelp_sample_unequal = chunk
    result = chunk.to_json(orient="records")
    with open("yelp_sample.json", "w") as f:
        json.dump(result, f)
    break

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