def solution(numbers):
    n = sorted(numbers)
    minus_max = n[0] * n[1]
    plus_max = n[-1] * n[-2]
    return max(minus_max, plus_max)