def solution(num_list):
    if num_list[-1] > num_list[-2]:
        last_num = [num_list[-1] - num_list[-2]]
    else:
        last_num = [num_list[-1] * 2]
    return num_list + last_num