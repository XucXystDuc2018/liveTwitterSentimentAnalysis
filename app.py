from flask import Flask, request, render_template
import pandas as pd
from ntscraper import Nitter
import re
from textblob import TextBlob

app = Flask(__name__)

scraper = Nitter(log_level=1, skip_instance_check=False)


def create_tweets_dataset(username, no_of_tweets):
    tweets = scraper.get_tweets(username, mode="user", number=no_of_tweets)
    data = {
        'link': [],
        'text': [],
        'user': [],
        'date': [],
        'likes': [],
        'quotes': [],
        'retweets': [],
        'comments': []
    }

    for tweet in tweets['tweets']:
        data['link'].append(tweet['link'])
        data['text'].append(tweet['text'])
        data['user'].append(tweet['user']['name'])
        data['date'].append(tweet['date'])
        data['likes'].append(tweet['stats']['likes'])
        data['quotes'].append(tweet['stats']['quotes'])
        data['retweets'].append(tweet['stats']['retweets'])
        data['comments'].append(tweet['stats']['comments'])

    df = pd.DataFrame(data)
    return df


def clean_tweet(tweet):
    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|([RT])', ' ', str(tweet).lower()).split())


def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    username = request.form['username']
    no_of_tweets = int(request.form['num_tweets'])
    df = create_tweets_dataset(username, no_of_tweets)
    df['clean_tweet'] = df['text'].apply(clean_tweet)
    df["sentiment"] = df["clean_tweet"].apply(analyze_sentiment)
    tweets = df.to_dict(orient='records')
    return render_template('results.html', tweets=tweets)


if __name__ == '__main__':
    app.run(debug=True)
