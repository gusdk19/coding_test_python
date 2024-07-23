import math
def solution(num_list):
    result = 1
    # return sum(num_list) if len(num_list) >= 11 else math.prod(num_list)
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in num_list:
            result *= i
        return result