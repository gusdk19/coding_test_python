def solution(slice, n):
    div = n // slice
    return div if n % slice == 0 else div + 1