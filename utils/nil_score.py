# nil_score.py
def calculate_score(score):
    if score >= 90:
        return "Elite readiness! You’re in top position for NIL deals."
    elif score >= 70:
        return "Strong potential. Just a few steps from being NIL-ready."
    elif score >= 50:
        return "You're on the radar. Start building your brand now."
    else:
        return "NIL readiness needs work. Let’s focus on your foundation."

def earnings_estimator(score):
    return round(score * 150)  # Base multiplier for simple mock model
