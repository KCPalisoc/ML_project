import pandas as pd
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import string
nltk.download('stopwords')
nltk.download('wordnet')
from sklearn.feature_extraction.text import CountVectorizer

#Change output_file_path to the path on your machine
stop_words = set(stopwords.words('english'))
punctuations = string.punctuation

#adding new_punct 
new_punct = '...,—…,“•”’'
punctuations = punctuations + new_punct

#adding additional stop word 
new_stopwords = 'rt'
stop_words.add(new_stopwords)

#Change the path to the path on your machine
df = pd.read_csv('Dashboard/Data/obamacare_19_23.csv')
tokenizer=TweetTokenizer()
df['Tokenized_Text'] = df['Text'].apply(tokenizer.tokenize)


def preprocessing_twts(tokens):
    '''
    '''
    tokens = [token.lower() for token in tokens]
    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]
    # Remove punctuations
    tokens = [token for token in tokens if token not in punctuations]
    return tokens

df['Tokenized_Text'] = df['Tokenized_Text'].apply(preprocessing_twts)

twitter_df = df.copy()
twitter_test_df = twitter_df.loc[:, ['Text']]
twitter_unigram_vocab = (CountVectorizer(ngram_range=(1,1), stop_words='english')
                         .fit(twitter_test_df.loc[:,'Text']))
twitter_test = twitter_unigram_vocab.transform(twitter_test_df.loc[:,'Text'])

#change to len(train_yelp_df) number of columns
twitter_test = twitter_test[:,:30110]