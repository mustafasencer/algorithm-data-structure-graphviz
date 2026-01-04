"""
Return the indice pairs of the nums array that result in the product value.
nums: [2, 1, 2, 4], product: 8
result: [(0, 3), (3, 0)]
"""


def solution(nums: list[int], product: int) -> list[int]:
    result = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] * nums[j] == product:
                result.append((i, j))

    return result


def solution_v2(nums: list[int], product: int) -> list[int]:
    result = []
    lookup = {}

    for i in range(len(nums)):
        if not product % nums[i] == 0:
            continue

        remaining = product // nums[i]

        if remaining in lookup:
            result.append((i, lookup[remaining]))
        else:
            lookup[remaining] = i

    return result


def solution_v3(nums: list[int], product: int) -> list[int]:
    # impossible to gather the indices with this method
    result = []

    def dfs(subset: list[int], current: list[int], target: int):
        nonlocal result

        if not subset:
            return

        if not target.is_integer():
            return

        if target == 1:
            result.append(tuple(current))
            return

        for i, val in enumerate(subset):
            if val == 1:
                continue
            dfs(subset[i:], [*current, val], target / val)

    dfs(nums, [], product)
    return result


if __name__ == "__main__":
    nums = [2, 1, 2, 4]
    product = 8
    result = solution_v2(nums, product)
    print(result)
