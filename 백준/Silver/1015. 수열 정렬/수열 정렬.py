import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
sortedA = sorted(A)
B = []

for i in A:
    B.append(sortedA.index(i))
    sortedA[sortedA.index(i)] = -1

print(*B)