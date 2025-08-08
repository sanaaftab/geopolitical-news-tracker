import requests
import pandas as pd
from datetime import date, timedelta


def fetch_news_country(api_key, country, keywords):
    """
    Fetch recent news for a country name using NewsAPI /v2/everything.
    Searches by country name and keywords. Date range fixed to last 21 days.
    """

    keyword_query = " OR ".join(keywords)
    query = f"({keyword_query}) AND {country}"

    to_date = date.today()
    from_date = to_date - timedelta(days=21)

    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "language": "en",
        "pageSize": 100,
        "sortBy": "publishedAt",
        "apiKey": api_key,
    }
    url = "https://newsapi.org/v2/everything"
    resp = requests.get(url, params=params)
    data = resp.json()

    articles = data.get("articles", [])
    df = pd.DataFrame([
        {
            "title": a.get("title"),
            "description": a.get("description"),
            "source": (a.get("source") or {}).get("name"),
            "publishedAt": a.get("publishedAt"),
            "url": a.get("url"),
        }
        for a in articles
    ])

    if not df.empty:
        df["publishedAt"] = pd.to_datetime(df["publishedAt"])  
    return df
