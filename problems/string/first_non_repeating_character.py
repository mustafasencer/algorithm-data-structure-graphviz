"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/
"""


def solution(chars):
    """
    1. Append the dict
    2. reloop and find the char that appears only once.
    """
    mapper = {}
    for char in chars:
        if char in mapper:
            mapper[char] += 1
            continue
        mapper[char] = 1
    for char in chars:
        if mapper[char] == 1:
            return char
    return -1


if __name__ == "__main__":
    chars = "hkgkadahskdh"
    result = solution(chars)
    assert result == "g"
