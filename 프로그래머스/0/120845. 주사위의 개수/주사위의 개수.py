def solution(box, n):
    result = 1
    for i in box:
        result *= i // n
    return result

# (가로 // n) * (세로 // n) * (높이 // n)