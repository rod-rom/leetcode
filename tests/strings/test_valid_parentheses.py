import pytest
from strings.valid_parentheses import is_valid_alt  # Adjust the import path

@pytest.mark.parametrize("input_str, expected_output", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("", True),
    ("[", False),
    ("]", False),
    ("([{}])", True),
    ("{[}](", False)
])
def test_is_valid_alt(input_str, expected_output):
    assert is_valid_alt(input_str) == expected_output
