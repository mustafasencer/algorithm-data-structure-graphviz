def solution(nums):
    """1."""
    result = []
    count = 0

    def dfs(nums, ans, result) -> None:
        nonlocal count
        if not nums:
            return

        if sum(ans) > sum(nums):
            result.append(ans)
            return

        for _ in range(1):
            count += 1
            dfs(nums[1:], [*ans, nums[0]], result)

    nums.sort(reverse=True)
    dfs(nums, [], result)
    return sorted(result, key=lambda x: (len(x), sum(x)))[0]


if __name__ == "__main__":
    nums = [2, 3, 4, 2, 5]
    result = solution(nums)
    assert result == [5, 4]
