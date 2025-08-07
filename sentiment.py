import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def analyze_sentiment(df):
    sia = SentimentIntensityAnalyzer()
    df["sentiment_score"] = df["description"].apply(lambda x: sia.polarity_scores(x)["compound"])
    return df
