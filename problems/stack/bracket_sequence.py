"""
https://leetcode.com/problems/valid-parentheses/description/
"""


def check_sequence(sequence) -> bool | None:
    bracket_mapper = {"{": "}", "[": "]", "(": ")"}
    reverse = ["}", ")", "]"]
    stack = []
    for char in sequence:
        if char in reverse:
            if not stack or bracket_mapper[stack.pop()] != char:
                return False
        else:
            stack.append(char)
    if not stack:
        return True
    return None


if __name__ == "__main__":
    sequence = "{{{}}}()[][]"
    result = check_sequence(sequence)
    assert result is True
