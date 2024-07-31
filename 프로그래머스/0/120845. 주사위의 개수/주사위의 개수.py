def solution(box, n):
    result = 1
    max_num = [i // n for i in box]
    for i in max_num:
        result *= i
    return result

# (가로 // n) * (세로 // n) * (높이 // n)