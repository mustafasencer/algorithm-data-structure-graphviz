"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N,
is called a slice of array A (notice that the slice contains at least two elements).
The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice.
 To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average.
If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""

import sys


def solution(A):
    """
    1. check the contiguous sub arrays having 2 and 3 items
    2. return the start index.
    """
    if len(A) == 2:
        return 0

    min_slice_two = A[0] + A[1]
    min_two_index = 0

    min_slice_three = sys.maxsize
    min_three_index = 0

    for i in range(2, len(A)):
        slice_two = sum(A[i - 1 : i + 1])
        if slice_two < min_slice_two:
            min_two_index = i - 1
            min_slice_two = slice_two

        slice_three = sum(A[i - 2 : i + 1])
        if slice_three < min_slice_three:
            min_three_index = i - 2
            min_slice_three = slice_three

    if min_slice_three * 2 < min_slice_two * 3:
        return min_three_index
    return min_two_index


def solution_v2(nums, k):
    """
    1. slightly different variation with known subarray size!
    2. return the subarray itself.
    """
    n = len(nums)

    # k must be smaller than or equal to n
    if n < k:
        return 0

    # Initialize beginning index of result
    res_index = 0

    # Compute sum of first subarray of size k
    curr_sum = 0
    for i in range(k):
        curr_sum += nums[i]

    # Initialize minimum sum as current sum
    min_sum = curr_sum

    # Traverse from (k + 1)'th element to n'th element
    for i in range(k, n):
        # Add current item and remove first item of previous subarray
        curr_sum -= nums[i - k]
        curr_sum += nums[i]

        # Update result if needed
        if curr_sum < min_sum:
            min_sum = curr_sum
            res_index = i - k + 1

    return nums[res_index : (res_index + k - 1)]


if __name__ == "__main__":
    A = [4, 2, 2, 5, 1, 5, 8]
    result = solution(A)
