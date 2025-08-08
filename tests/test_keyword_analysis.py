import pandas as pd
import keyword_analysis

def test_get_keyword_frequencies_basic():
    df = pd.DataFrame({"description": ["conflict war protest", "war protest"]})
    keywords = ["conflict", "war", "protest"]
    freq = keyword_analysis.get_keyword_frequencies(df, keywords)
    assert freq["conflict"] == 1
    assert freq["war"] == 2
    assert freq["protest"] == 2
