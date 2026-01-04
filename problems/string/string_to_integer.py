def solution(s: str) -> int:
    s = s.strip()
    if not s:
        return 0

    sign = 1
    if s[0] == "-":
        sign = -1
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]

    result = 0
    for i in range(len(s)):
        if not s[i].isdigit():
            break
        result = result * 10 + int(s[i])

    result *= sign
    if result < -(2**31):
        return -(2**31)
    if result > 2**31 - 1:
        return 2**31 - 1

    return result
