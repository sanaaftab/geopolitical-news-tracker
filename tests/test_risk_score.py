import risk_score

def test_calculate_risk_score_typical():
    score = risk_score.calculate_risk_score(25, 0.0)
    assert 0 <= score <= 100

def test_calculate_risk_score_max():
    score = risk_score.calculate_risk_score(100, -1.0)
    assert score == 100.0

def test_get_recommendation():
    assert risk_score.get_recommendation(55) == "High risk – Recommend delaying entry"
    assert risk_score.get_recommendation(45) == "Moderate risk – Monitor closely"
    assert risk_score.get_recommendation(30) == "Low risk – Consider entering"
