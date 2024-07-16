def solution(num, total):
    answer = []
    mid = total // num
    if(num % 2 == 1):
        for i in range(mid - num//2, mid + num//2 + 1):
            answer.append(i)
    else:
        for i in range(mid - num//2 + 1, mid + num//2 + 1):
            answer.append(i)
    return answer