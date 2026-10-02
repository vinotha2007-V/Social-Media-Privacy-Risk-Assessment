
RECOMMENDATIONS = {
    "profile_visibility": {
        "threshold": 40,
        "advice": "Review your profile visibility and limit access to trusted audiences.",
    },
    "personal_information": {
        "threshold": 40,
        "advice": "Avoid publicly sharing personal details such as your phone number or home address.",
    },
    "location_privacy": {
        "threshold": 40,
        "advice": "Review location permissions and avoid posting your live location publicly.",
    },
    "posts_content": {
        "threshold": 40,
        "advice": "Review older public posts and check photos for sensitive information.",
    },
    "friends_followers": {
        "threshold": 40,
        "advice": "Review your followers and remove unfamiliar or untrusted accounts.",
    },
    "tagging_mentions": {
        "threshold": 40,
        "advice": "Review tagging settings and enable tag approval where available.",
    },
    "account_security": {
        "threshold": 40,
        "advice": "Use a unique password and enable multi-factor authentication.",
    },
    "third_party_apps": {
        "threshold": 40,
        "advice": "Review connected apps and revoke permissions you no longer need.",
    },
    "messaging_safety": {
        "threshold": 40,
        "advice": "Be cautious with unexpected links, suspicious messages, and requests for personal data.",
    },
    "digital_footprint": {
        "threshold": 40,
        "advice": "Search for your public profile information and review what you choose to share.",
    },
}


def generate_recommendations(category_results):
    """Generate privacy advice for categories with elevated risk."""

    recommendations = []

    for category, result in category_results.items():
        score = result["risk_score"]

        if category not in RECOMMENDATIONS:
            continue

        rule = RECOMMENDATIONS[category]

        if score > rule["threshold"]:
            recommendations.append({
                "category": result["category_name"],
                "risk_score": score,
                "recommendation": rule["advice"],
            })

    return recommendations


if __name__ == "__main__":
    sample_results = {
        "profile_visibility": {
            "category_name": "Profile Visibility",
            "risk_score": 83,
        },
        "account_security": {
            "category_name": "Authentication and Account Security",
            "risk_score": 25,
        },
        "location_privacy": {
            "category_name": "Location Privacy",
            "risk_score": 58,
        },
    }

    suggestions = generate_recommendations(sample_results)

    print("PRIVACY RECOMMENDATIONS")
    print("-" * 35)

    for item in suggestions:
        print(f"\nCategory: {item['category']}")
        print(f"Risk: {item['risk_score']}/100")
        print(f"Advice: {item['recommendation']}")