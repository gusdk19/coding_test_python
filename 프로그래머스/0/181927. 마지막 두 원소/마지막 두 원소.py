def solution(num_list):
    if num_list[-1] > num_list[-2]:
        last_num = num_list[-1] - num_list[-2]
    else:
        last_num = num_list[-1] * 2
    num_list.append(last_num)
    return num_list