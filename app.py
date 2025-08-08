import os
import streamlit as st
import pandas as pd
from fetch_news import fetch_news_country
from keyword_analysis import get_keyword_frequencies
from sentiment import analyze_sentiment
from risk_score import calculate_risk_score, get_recommendation
from utils import validate_country_name

# --------------- Secure API Key Retrieval ---------------
def get_api_key():
    return os.environ.get("NEWSAPI_KEY")

# ---------------- App Setup ----------------
st.set_page_config(page_title="Geopolitical Risk Tracker", layout="wide")
st.title("Geopolitical Risk Tracker")
st.markdown("Analyze country-level geopolitical risk using the past 3 weeks of news.")

# ---------------- User Inputs --------------
st.sidebar.header("Parameters")
country = st.sidebar.text_input("Country", "Iran")

api_key = get_api_key()
run_button = st.sidebar.button("Run Analysis")

# Default keyword set used internally (UI does not expose keywords)
DEFAULT_KEYWORDS = [
    "conflict", "war", "protest", "unrest", "military", "coup", "sanctions",
    "strike", "riot", "bombing", "missile", "ceasefire", "invasion",
    "corruption", "power struggle", "diplomatic tension"
]

# ---------------- Main Logic ---------------
if run_button:

    if not validate_country_name(country):
        st.error("Invalid country name. Please enter a valid country.")
    else:
        st.subheader(f"Results for {country} (last 30 days)")

        if not api_key:
            st.error("Missing API key. Set NEWSAPI_KEY as an environment variable.")
        else:
            df = fetch_news_country(api_key, country, DEFAULT_KEYWORDS)

            if df.empty:
                st.warning("No articles found. Try a different country.")
            else:
                st.success(f"Fetched {len(df)} articles.")

                # Keyword frequency (using a fixed list)
                kw_freq = get_keyword_frequencies(df, DEFAULT_KEYWORDS)
                display_data = [(kw, kw_freq.get(kw, 0)) for kw in DEFAULT_KEYWORDS]

                st.subheader("Keyword Frequency")
                freq_df = (
                    pd.DataFrame(display_data, columns=["Keyword", "Count"])
                    .sort_values(by="Count", ascending=False)
                )
                st.bar_chart(freq_df.set_index("Keyword"))

                # Sentiment analysis
                df = analyze_sentiment(df)
                st.subheader("Sentiment Over Time")
                df_sorted = df.sort_values("publishedAt")
                st.line_chart(df_sorted.set_index("publishedAt")["sentiment_score"])

                # Risk score with fixed normalization baseline
                avg_sent = df["sentiment_score"].mean()
                total_hits = sum(kw_freq.values())
                risk = calculate_risk_score(total_hits, avg_sent)

                st.subheader("Risk Assessment")
                st.metric("Risk Score", f"{risk}")
                st.info(get_recommendation(risk))
