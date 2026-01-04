def solution(s: str, word_dict: list[str]) -> bool:
    """
    1. Create a dp list with the same length as the input string.
    2. Iterate over the input string.
    3. Iterate over the word dictionary.
    4. Check if the current word in the dictionary is equal to the current substring.
    5. Check if the previous substring is True or that it is the first word in the string (i - len(w) == -1).
    6. Update the dp list.
    7. Return the last element in the dp list.
    """
    dp = [False] * len(s)
    for i in range(len(s)):
        for w in word_dict:
            if s[i - len(w) + 1 : i + 1] == w and (dp[i - len(w)] or i - len(w) == -1):
                dp[i] = True
    return dp[-1]


if __name__ == "__main__":
    result = solution("leetcode", ["leet", "code"])
    assert result is True
