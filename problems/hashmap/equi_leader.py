def solution(A):
    """1. Hard: Not yet done."""
    lookup = {}

    for i in range(len(A)):
        if A[i] in lookup:
            lookup[A[i]] += 1
        else:
            lookup[A[i]] = 1

    max_value = 0
    max_key = 0
    for k, v in lookup.items():
        if v > max_value:
            max_value = v
            max_key = k

    if max_value <= len(A) / 2:
        return 0

    leader_count = 0
    equi_leader_count = 0
    for i in range(len(A)):
        if A[i] == max_key:
            leader_count += 1

        if (
            i + 1 != len(A)
            and leader_count > (len(A[: i + 1]) / 2)
            and (max_value - leader_count) > (len(A[i + 1 :]) / 2)
        ):
            equi_leader_count += 1

    return equi_leader_count


if __name__ == "__main__":
    A = [1, 2, 1, 1, 2, 1]
    result = solution(A)
    assert result == 3
