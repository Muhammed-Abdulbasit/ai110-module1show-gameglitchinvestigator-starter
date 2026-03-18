import pytest
from app import check_guess

def test_check_guess():
    # Test case where guess is less than secret
    outcome, message = check_guess(5, 10)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

    # Test case where guess is greater than secret
    outcome, message = check_guess(15, 10)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

    # Test case where guess is equal to secret
    outcome, message = check_guess(10, 10)
    assert outcome == "Win"
    assert message == "🎉 Correct!"
