def solution(num_list):
    # odd = sum([num for i, num in enumerate(num_list) if i%2==1])
    # even = sum([num for i, num in enumerate(num_list) if i%2 == 0])
    odd = sum(num_list[::2])
    even = sum(num_list[1::2])
    return max(odd, even)