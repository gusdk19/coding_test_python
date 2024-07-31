def solution(n):
    # result = 0
    # n_list = [i for i in str(n)]
    # for j in n_list:
    #     result += int(j)
    # return result
    return sum([int(i) for i in str(n)])