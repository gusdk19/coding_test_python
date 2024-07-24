def solution(my_string, is_prefix):
    prefix_string = [i for i in my_string[:len(is_prefix)]]
    if prefix_string == list(is_prefix):
        return 1
    else:
        return 0