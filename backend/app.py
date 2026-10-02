
from flask import Flask, request, jsonify
from flask_cors import CORS

from risk_engine import analyze_privacy_risk
from category_analyzer import analyze_categories
from recommendations import generate_recommendations
from database import (
    initialize_database,
    save_assessment,
    get_all_assessments,
)

app = Flask(__name__)
CORS(app)

initialize_database()


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Social Media Privacy Risk Assessment API",
        "status": "running"
    })


@app.route("/api/assess", methods=["POST"])
def assess():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON request body is required."}), 400

    answers = data.get("answers")

    if not isinstance(answers, list):
        return jsonify({"error": "answers must be a list."}), 400

    try:
        result = analyze_privacy_risk(answers)

        category_answers = data.get("categories")
        category_results = None

        if category_answers is not None:
            category_results = analyze_categories(category_answers)

            category_scores = [
                item["risk_score"]
                for item in category_results.values()
            ]

            if not category_scores:
                return jsonify({
                    "error": "At least one category is required."
                }), 400

            overall_score = round(
                sum(category_scores) / len(category_scores)
            )

            if overall_score <= 20:
                risk_level = "LOW"
            elif overall_score <= 40:
                risk_level = "MODERATE"
            elif overall_score <= 70:
                risk_level = "HIGH"
            else:
                risk_level = "CRITICAL"

            result = {
                "risk_score": overall_score,
                "risk_level": risk_level,
                "total_questions": sum(
                    item["total_questions"]
                    for item in category_results.values()
                )
            }

    except (ValueError, TypeError) as error:
        return jsonify({"error": str(error)}), 400

    assessment_id = save_assessment(result, category_results)

    response = {
        "assessment_id": assessment_id,
        **result
    }

    if category_results is not None:
        response["categories"] = category_results
        response["recommendations"] = generate_recommendations(
            category_results
        )

    return jsonify(response), 201


@app.route("/api/assessments", methods=["GET"])
def assessments():
    return jsonify({
        "assessments": get_all_assessments()
    })


@app.route("/api/categories", methods=["POST"])
def categories():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON request body is required."}), 400

    category_answers = data.get("categories")

    if not isinstance(category_answers, dict) or not category_answers:
        return jsonify({
            "error": "categories must be a non-empty object."
        }), 400

    try:
        results = analyze_categories(category_answers)
    except (ValueError, TypeError) as error:
        return jsonify({"error": str(error)}), 400

    return jsonify({
        "categories": results,
        "recommendations": generate_recommendations(results)
    })


if __name__ == "__main__":
    app.run(debug=True)