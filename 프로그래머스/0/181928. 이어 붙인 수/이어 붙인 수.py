def solution(num_list):
    odd_str = ''
    even_str = ''
    for i in num_list:
        if i % 2 == 1:
            odd_str+=str(i)
        else:
            even_str+=str(i)
    return int(odd_str) + int(even_str)