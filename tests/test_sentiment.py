
import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sentiment

def test_analyze_sentiment_adds_column():
    df = pd.DataFrame({"description": ["good news", "bad news"]})
    result = sentiment.analyze_sentiment(df)
    assert "sentiment_score" in result.columns
    assert len(result) == 2
