from collections import defaultdict


def solution(strs: list[str]) -> list[list[str]]:
    memo = {}
    for item in strs:
        sort_ = "".join(sorted(item))
        if sort_ in memo:
            memo[sort_].append(item)
        else:
            memo[sort_] = [item]
    return [v for k, v in memo.items()]


def solution_1(strs: list[str]):
    lookup = defaultdict(list)

    for item in strs:
        key = "".join(sorted(item))
        lookup[key].append(item)

    return [value for _, value in lookup.items()]


if __name__ == "__main__":
    result = solution_1(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert result == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
