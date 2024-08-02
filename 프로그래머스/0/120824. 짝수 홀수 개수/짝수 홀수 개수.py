def solution(num_list):
    even = [i for i in num_list if i%2==0]
    odd = [i for i in num_list if i%2]
    return len(even), len(odd)