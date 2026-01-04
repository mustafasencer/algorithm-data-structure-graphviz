"""Codewars:
A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).

Within that sequence, he chooses two numbers, a and b.

He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.

Given a number n, could you tell me the numbers he excluded from the sequence?

The function takes the parameter: n (n is always strictly greater than 0) and returns an array of arrays.
"""


def remove_nb(n):
    sum = n * (n + 1) / 2

    def _apply():
        for a in range(1, n + 1):
            b = (sum - a) / (a + 1)
            if b.is_integer() and b <= n:
                yield (a, int(b))

    result = _apply()
    return list(result)


if __name__ == "__main__":
    result = remove_nb(5)
    print(result)
