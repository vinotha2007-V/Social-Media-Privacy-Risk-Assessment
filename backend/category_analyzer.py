
from risk_engine import calculate_risk_score

PRIVACY_CATEGORIES = {
    "profile_visibility": "Profile Visibility",
    "personal_information": "Personal Information",
    "location_privacy": "Location Privacy",
    "posts_content": "Posts and Content",
    "friends_followers": "Friends and Followers",
    "tagging_mentions": "Tagging and Mentions",
    "account_security": "Authentication and Account Security",
    "third_party_apps": "Third-Party Applications",
    "messaging_safety": "Messaging and Social Engineering",
    "digital_footprint": "Digital Footprint",
}


def analyze_categories(category_answers):
    """Calculate privacy risk scores for each category."""

    if not isinstance(category_answers, dict):
        raise ValueError("Category answers must be a dictionary.")

    if not category_answers:
        raise ValueError("At least one category is required.")

    results = {}

    for category, answers in category_answers.items():
        if category not in PRIVACY_CATEGORIES:
            raise ValueError(f"Unknown category: {category}")

        if not isinstance(answers, list) or not answers:
            raise ValueError(
                f"Answers for {category} must be a non-empty list."
            )

        score = calculate_risk_score(answers)

        results[category] = {
            "category_name": PRIVACY_CATEGORIES[category],
            "risk_score": score,
            "risk_level": (
                "LOW" if score <= 20 else
                "MODERATE" if score <= 40 else
                "HIGH" if score <= 70 else
                "CRITICAL"
            ),
            "total_questions": len(answers),
        }

    return results


if __name__ == "__main__":
    sample_data = {
        "profile_visibility": [3, 4, 2, 3],
        "personal_information": [4, 3, 4, 4],
        "location_privacy": [2, 3, 2, 1],
        "account_security": [1, 2, 1, 0],
    }

    results = analyze_categories(sample_data)

    print("CATEGORY-WISE PRIVACY RISK")
    print("-" * 40)

    for item in results.values():
        print(
            f"{item['category_name']}: "
            f"{item['risk_score']}/100 - "
            f"{item['risk_level']}"
        )