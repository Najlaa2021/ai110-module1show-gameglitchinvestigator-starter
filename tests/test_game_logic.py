from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the bug fixed this session ---
# Symptom: guessing 7 said "go higher" AND guessing 100 also said "go higher".
# Cause: the hint direction was reversed, and on some attempts the secret was
# turned into a string, so guesses were compared as TEXT ("7" > "50" is True).

def test_too_high_hint_says_go_lower():
    # A guess above the secret must tell the player to go LOWER, not higher.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_too_low_hint_says_go_higher():
    # A guess below the secret must tell the player to go HIGHER, not lower.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()


def test_no_string_comparison_glitch():
    # The exact reported symptom: with secret 50, 7 is too LOW and 100 is too HIGH.
    # A text comparison would wrongly call "7" too high and "100" too low.
    assert check_guess(7, 50)[0] == "Too Low"
    assert check_guess(100, 50)[0] == "Too High"


def test_numeric_comparison_even_with_string_inputs():
    # Numbers passed as strings must still compare numerically, not lexically.
    assert check_guess("7", "50")[0] == "Too Low"
    assert check_guess("100", "50")[0] == "Too High"
