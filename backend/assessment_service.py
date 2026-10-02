
from category_analyzer import analyze_categories
from recommendations import generate_recommendations


def build_assessment_report(category_answers):
    """Build category scores and recommendations for an assessment."""

    category_results = analyze_categories(category_answers)
    recommendations = generate_recommendations(category_results)

    scores = [
        item["risk_score"]
        for item in category_results.values()
    ]

    overall_score = round(sum(scores) / len(scores)) if scores else 0

    if overall_score <= 20:
        risk_level = "LOW"
    elif overall_score <= 40:
        risk_level = "MODERATE"
    elif overall_score <= 70:
        risk_level = "HIGH"
    else:
        risk_level = "CRITICAL"

    return {
        "overall_score": overall_score,
        "risk_level": risk_level,
        "categories": category_results,
        "recommendations": recommendations,
    }


if __name__ == "__main__":
    sample_answers = {
        "profile_visibility": [3, 4, 2],
        "personal_information": [4, 3, 4],
        "location_privacy": [2, 3, 2],
        "posts_content": [3, 2, 3],
        "friends_followers": [2, 2, 3],
        "tagging_mentions": [2, 3, 2],
        "account_security": [1, 2, 1],
        "third_party_apps": [3, 2, 3],
        "messaging_safety": [2, 3, 2],
        "digital_footprint": [3, 3, 2],
    }

    report = build_assessment_report(sample_answers)

    print("PRIVACY ASSESSMENT REPORT")
    print("-" * 35)
    print("Overall Score:", report["overall_score"], "/100")
    print("Risk Level:", report["risk_level"])
    print("\nCATEGORY SCORES:")

    for item in report["categories"].values():
        print(f"{item['category_name']}: {item['risk_score']}/100")

    print("\nRECOMMENDATIONS:")

    for item in report["recommendations"]:
        print(f"- {item['category']}: {item['recommendation']}")