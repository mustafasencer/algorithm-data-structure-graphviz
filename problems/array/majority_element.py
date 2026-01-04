"""
https://leetcode.com/problems/majority-element/description/
"""


def solution(nums):
    """1. No explanation!"""
    nums.sort()
    return nums[len(nums) // 2]


def solution_2(nums):
    """1."""
    m = {}
    for n in nums:
        m[n] = m.get(n, 0) + 1
        if m[n] > len(nums) // 2:
            return n
    return None


def solution_3(nums):
    """1. No explanation!"""
    candidate, count = nums[0], 0
    for num in nums:
        if num == candidate:
            count += 1
        elif count == 0:
            candidate, count = num, 1
        else:
            count -= 1
    return candidate


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 2, 2, 2]
    result = solution(nums)
    assert result == 2
