import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def analyze_sentiment(df):
    """ Analyze sentiment scores using VADER.

    Args: df: DataFrame containing a 'description' column.

    Returns: df: An added 'sentiment_score' column containing sentiment scores. """
    sia = SentimentIntensityAnalyzer()
    df["sentiment_score"] = df["description"].apply(lambda x: sia.polarity_scores(x)["compound"])
    return df
