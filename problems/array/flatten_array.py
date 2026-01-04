from typing import Any

"""
https://leetcode.com/problems/flatten-deeply-nested-array/description/
"""


def flatten_recursive(L: list) -> list[Any]:
    """
    1. check whether 1st item is a list
    2. recursively flatten that item and the rest of the outer list
    3. don't forget to implement exit conditions!
    """
    if not L:
        return []
    if isinstance(L[0], list):
        return flatten_recursive(L[0]) + flatten_recursive(L[1:])
    return [L[0], *flatten_recursive(L[1:])]


def flatten_stack(L: list) -> list[Any]:
    """
    1. append all items into stack
    2. pop stack by checking the popped item's type
    3. return the reversed result.
    """
    stack = []
    result = []
    for item in L:
        stack.append(item)

    while stack:
        item = stack.pop()

        if isinstance(item, list):
            for i in item:
                stack.append(i)
            continue

        result.append(item)

    return result[::-1]


if __name__ == "__main__":
    L = [[1, [2, 3]], [2]]
    result = flatten_stack(L)
