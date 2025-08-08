# geopolitical-news-tracker

# Geopolitical Risk Tracker

This project is a Streamlit-based web app that analyzes geopolitical risks by collecting recent news articles about a given country and evaluating them using keyword frequency and sentiment analysis.

## Features

* Fetches news using **NewsAPI**
* Performs **keyword frequency analysis**
* Conducts **sentiment analysis** using VADER
* Calculates a **geopolitical risk score** based on keyword hits and sentiment
* Provides an **actionable recommendation** (low, moderate, or high risk)
* Visualizes keyword frequency and sentiment trends

## Project Structure

```
geo-risk-tracker/
├── app.py                   # Main Streamlit app
├── fetch_news.py           # NewsAPI handlers
├── keyword_analysis.py     # Keyword frequency analysis
├── sentiment.py            # Sentiment analysis (VADER)
├── risk_score.py           # Risk scoring logic
├── utils.py                # Country code lookup, date range
├── requirements.txt        # Python dependencies
├── tests/                       # Unit tests for project modules
│   ├── test_keyword_analysis.py
│   ├── test_sentiment.py
│   └── test_risk_score.py 
└── README.md
```

## Setup Instructions

1. **Clone this repo**

```bash
git clone https://github.com/YOUR_USERNAME/geo-risk-tracker.git
cd geo-risk-tracker
```

2. **Create a virtual environment (optional but recommended)**

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run app.py
```

## API Key Setup

* Get your **NewsAPI key** from: [https://newsapi.org](https://newsapi.org)
* Please set it up as an environment variable under NEWSAPI_KEY

nano ~/.zshrc                                   # 1. Open shell profile
export NEWSAPI_KEY="your_newsapi_key_here"      # 2. Add this line at the end
source ~/.zshrc                                 # 3. Reload profile
echo $NEWSAPI_KEY                               # 4. Verify it was set

## Sample Use Case

Analyze the risk level in your chosen country over the past 21 days using keywords like:

```
conflict, war, protest, unrest, sanctions, bombing
```

The app will output:

* Keyword frequency bar chart
* Sentiment score line chart
* Overall risk score and recommendation


Made for NYU Stern MBA – Programming in Python and Fundamentals of Software Development

