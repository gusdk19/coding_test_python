def solution(a, b):
    if (a > b):
        a, b = b, a
    dif = b - a + 1
    answer = 0
    for i in range(dif):
        answer += a + i
    return answer