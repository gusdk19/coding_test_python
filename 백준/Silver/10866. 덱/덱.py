import sys
input = sys.stdin.readline

from collections import deque
N = int(input()) # 명령의 수

dq = deque()
# print(dq)
for i in range(N):
    comm = input().split()
    if(comm[0] == 'push_front'):
        dq.appendleft(comm[1])
    if(comm[0] == 'push_back'):
        dq.append(comm[1])
    if(comm[0] == 'pop_front'):
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())
    if(comm[0] == 'pop_back'):
        if len(dq)==0:
            print(-1)
        else:
            print(dq.pop())
    if(comm[0] == 'size'):
        print(len(dq))
    if(comm[0] == 'empty'):
        if dq:
            print(0)
        else:
            print(1)
    if(comm[0] == 'front'):
        if dq:
            print(dq[0])
        else:
            print(-1)
    if(comm[0] == 'back'):
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])
    # print('현재 dq', dq)