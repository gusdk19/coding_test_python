def solution(n):
    arr = [[0 if j!=i else 1 for j in range(n)] for i in range(n)]
    return arr