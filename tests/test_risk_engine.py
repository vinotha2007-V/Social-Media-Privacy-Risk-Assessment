
import pytest

from backend.risk_engine import (
    calculate_risk_score,
    classify_risk,
    analyze_privacy_risk,
)


def test_calculate_risk_score():
    assert calculate_risk_score([4, 4, 4, 4]) == 100
    assert calculate_risk_score([0, 0, 0, 0]) == 0
    assert calculate_risk_score([2, 2, 2, 2]) == 50


def test_classify_risk():
    assert classify_risk(10) == "LOW"
    assert classify_risk(30) == "MODERATE"
    assert classify_risk(60) == "HIGH"
    assert classify_risk(80) == "CRITICAL"


def test_empty_answers():
    with pytest.raises(ValueError):
        calculate_risk_score([])


def test_invalid_answers():
    with pytest.raises(ValueError):
        calculate_risk_score([5])

    with pytest.raises(ValueError):
        calculate_risk_score([-1])


def test_analyze_privacy_risk():
    result = analyze_privacy_risk([4, 4, 4, 4])

    assert result["risk_score"] == 100
    assert result["risk_level"] == "CRITICAL"
    assert result["total_questions"] == 4