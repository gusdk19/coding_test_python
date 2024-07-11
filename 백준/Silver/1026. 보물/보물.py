import sys
input = sys.stdin.readline

N = int(input())
A = []
B = []

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
B.reverse()


result = [i*j for i, j in zip(A, B)]
total_min = sum(result)

print(total_min)