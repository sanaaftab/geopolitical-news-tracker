import nltk
import re
from collections import Counter
from nltk.stem import PorterStemmer

nltk.download("punkt_tab")

def get_keyword_frequencies(df, keywords):
    """ Calculate the frequency of keywords in the 'description' column.

    Args: df: DataFrame containing a 'description' column with text data. 
    keywords (list of str): List of keywords to search for in the descriptions.

    Returns: dict: A dictionary of each stemmed keyword to its frequency count. """

    ps = PorterStemmer()
    stemmed_keywords = [ps.stem(kw.lower()) for kw in keywords]

    descriptions = " ".join(df["description"].fillna("")).lower()
    words = nltk.word_tokenize(descriptions)
    stemmed_words = [ps.stem(word) for word in words]
    word_counts = Counter(stemmed_words)
    freq = {kw: word_counts[kw] for kw in stemmed_keywords}
    return freq

