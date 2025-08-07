def calculate_risk_score(keyword_count, avg_sentiment):
    # Variable to indicate high instability
    # E.g. if country has 50+ counts of the keywords, it indicates max instability
    max_keyword_possible = 50
    norm_keyword_score = min(keyword_count / max_keyword_possible, 1.0)

    # Normalize sentiment from -1 (bad)-> 1 (good) to 1 -> 0 scale
    norm_sentiment_score = 1 - ((avg_sentiment + 1) / 2)

    keyword_weight = 0.4
    sentiment_weight = 0.6
    risk_score = (keyword_weight * norm_keyword_score + sentiment_weight * norm_sentiment_score) * 100

    return round(risk_score, 1)


def get_recommendation(risk_score):
    if risk_score >= 50:
        return "High risk – Recommend delaying entry"
    elif risk_score >= 40:
        return "Moderate risk – Monitor closely"
    else:
        return "Low risk – Consider entering"
