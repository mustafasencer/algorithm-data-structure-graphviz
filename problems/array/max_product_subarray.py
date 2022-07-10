"""
    Created by Mustafa Sencer Özcan on 26.05.2020.

    Given an integer array nums, find the contiguous subarray
    within an array (containing at least one number) which has the largest product.
"""
from functools import reduce
from typing import List


class Solution:
    def max_product(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            k = i + 1
            while k < len(nums):
                result = max(reduce(lambda x, y: x * y, nums[i : k + 1]), result, 0)
                k += 1
        return result

    def _test(self, nums):
        nums_copy = nums[::-1]
        for i in range(len(nums)):
            nums[i] *= nums[i - 1] or 1
            nums_copy[i] *= nums[i - 1] or 1
        return max(nums + nums_copy)

    def test_(self, nums):
        max_product = 0
        for i in range(len(nums)):
            k = i + 1
            product_start = nums[i]
            while k < len(nums):
                product_start = product_start * nums[k]
                max_product = max(product_start, 0, max_product)
                k += 1
        return max_product


if __name__ == "__main__":
    result = Solution()._test([-2, 2, 3, -1, 3, 9])
    assert result == 2916
    print(result)