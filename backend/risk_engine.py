
RISK_LEVELS = {
    "LOW": (0, 20),
    "MODERATE": (21, 40),
    "HIGH": (41, 70),
    "CRITICAL": (71, 100),
}


def calculate_risk_score(answers):
    """Calculate a privacy risk score from 0 to 100."""

    if not answers:
        raise ValueError("At least one answer is required.")

    for answer in answers:
        if (
            not isinstance(answer, int)
            or isinstance(answer, bool)
            or answer < 0
            or answer > 4
        ):
            raise ValueError("Each answer must be an integer from 0 to 4.")

    average = sum(answers) / len(answers)
    return round((average / 4) * 100)


def classify_risk(score):
    """Classify the calculated privacy risk score."""

    if not isinstance(score, int) or isinstance(score, bool):
        raise ValueError("Score must be an integer.")

    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    for level, (minimum, maximum) in RISK_LEVELS.items():
        if minimum <= score <= maximum:
            return level


def analyze_privacy_risk(answers):
    """Return the risk score, level, and number of answers."""

    score = calculate_risk_score(answers)

    return {
        "risk_score": score,
        "risk_level": classify_risk(score),
        "total_questions": len(answers),
    }


if __name__ == "__main__":
    sample_answers = [4, 3, 2, 4, 3, 2, 3, 4, 1, 3]

    result = analyze_privacy_risk(sample_answers)

    print("Social Media Privacy Risk Assessment")
    print("------------------------------------")
    print(f"Risk Score : {result['risk_score']}/100")
    print(f"Risk Level : {result['risk_level']}")
    print(f"Questions  : {result['total_questions']}")