def solution(n):
    result = [n]
    while(1):
        if n==1:
            return result
            break
        else:
            if n%2==0:
                n = n // 2
                result.append(n)
            else:
                n = 3 * n + 1
                result.append(n)
                