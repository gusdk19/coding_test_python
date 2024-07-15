def solution(t, p):
    cnt = 0
    list_t = []
    for i in range(0, len(t) - len(p) + 1):
        # list_t.append()
        if(t[i:i+len(p)] <= p):
            cnt += 1
    return cnt