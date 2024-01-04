from Dashboard.load_and_clean.tweet_preprocess import twitter_df
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from wordcloud import WordCloud
import plotly.express as px

# Convert the tweet date column to a datetime format
twitter_df['Date'] = pd.to_datetime(twitter_df['Date'])
twitter_df = twitter_df.set_index('Date')

# Calculate the average tweet count per day
daily_tweets = twitter_df.resample('D').size()
avg_daily_tweets = daily_tweets.mean()

# Plot the average tweet count per day
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(daily_tweets.index, daily_tweets, color='blue')
ax.axhline(y=avg_daily_tweets, color='red', linestyle='--')
ax.set(xlabel='Date', ylabel='Tweet Count', title='Average Tweet Count per Day')
ax.grid()

# Calculate the average tweet count by day of the week
day_of_week_tweets = twitter_df.groupby(twitter_df.index.dayofweek).size()
avg_day_of_week_tweets = day_of_week_tweets.mean()

# Plot the average tweet count by day of the week
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(day_of_week_tweets.index, day_of_week_tweets, color='blue')
ax.axhline(y=avg_day_of_week_tweets, color='red', linestyle='--')
ax.set(xlabel='Day of Week', ylabel='Tweet Count', title='Average Tweet Count by Day of Week')
ax.set_xticklabels(['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
ax.grid()

# Calculate the average tweet count by month
monthly_tweets = twitter_df.resample('M').size()
avg_monthly_tweets = monthly_tweets.mean()

# Plot the average tweet count by month
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(monthly_tweets.index, monthly_tweets, color='blue')
ax.axhline(y=avg_monthly_tweets, color='red', linestyle='--')
ax.set(xlabel='Month', ylabel='Tweet Count', title='Average Tweet Count by Month')
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.grid()

# Format the x-axis tick labels
labels = [pd.to_datetime(str(x)).strftime('%B %Y') for x in monthly_tweets.index]
ax.set_xticklabels(labels, rotation=45, ha='right')


dfc = twitter_df.copy()
dfc = dfc.loc[:,'Tokenized_Text']

def tweet_bar(top_100_words, top_100_count, token):

    fig = px.bar(top_100_words, top_100_count)
    if token == '#':
        fig.update_layout(title_text='Top 100 Hashtags')
    elif token == '@':
        fig.update_layout(title_text='Top 100 Ats')
    else:
        fig.update_layout(title_text='Top 100 Words')

def word_dict(dfc, token):
    """
    """

    word_dict = {}
    for _, row in dfc.items():
        for word in row:
            if word[0] == token:
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1

    sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    top_100 = sorted_dict[:100]
    top_100_words = [item[0] for item in top_100]
    top_100_count = [item[1] for item in top_100]

    return top_100_words, top_100_count

def freq_word_cloud():
    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                min_font_size = 10).generate_from_frequencies(frequencies = word_dict)

    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)

def n_gram(n):
    total_lst =[]
    for index, row in dfc.items():
        n_gram_lst = []
        for i in range(0, len(row)-n+1):
            n_gram_lst.append(tuple(row[i: i + n]))
        total_lst.append(n_gram_lst)
    return total_lst

trigram = n_gram(3)
bigram = n_gram(2)

def ngram_count_dict(n_gram_lst):
    
    ngram_dict = {}
    for row in n_gram_lst:
        for word in row:
                if word not in ngram_dict:
                    ngram_dict[word] = 1
                else:
                    ngram_dict[word] += 1
    return ngram_dict


tri_count_dict = ngram_count_dict(trigram)
bi_count_dict = ngram_count_dict(bigram)
sorted_dict = sorted(tri_count_dict.items(), key=lambda x: x[1], reverse=True)
top_100 = sorted_dict[:100]
top_100_words = [str(item[0]) for item in top_100]
top_100_count = [item[1] for item in top_100]

def plot_ngram():

    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.bar(top_100_words, top_100_count)
    plt.xticks(rotation = 90)
    plt.xlabel('Trigrams')
    plt.ylabel('Count')
    plt.title('Top 100 Twitters Trigrams')

new_tri_dict = {}
for key, value in  tri_count_dict.items():
    new_key = str(key)
    new_tri_dict[new_key] = value

def ngram_word_cloud():

    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                min_font_size = 10).generate_from_frequencies(frequencies = new_tri_dict)

    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)


sorted_dict = sorted(bi_count_dict.items(), key=lambda x: x[1], reverse=True)
top_100 = sorted_dict[:100]
top_100_words = [str(item[0]) for item in top_100]
top_100_count = [item[1] for item in top_100]

new_bi_dict = {}
for key, value in  bi_count_dict.items():
    new_key = str(key)
    new_bi_dict[new_key] = value
