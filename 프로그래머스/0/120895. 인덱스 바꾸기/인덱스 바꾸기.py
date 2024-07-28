def solution(my_string, num1, num2):
    # str = ''
    # for i in range(len(my_string)):
    #     if i == num1:
    #         str += my_string[num2]
    #     elif i == num2:
    #         str += my_string[num1]
    #     else:
    #         str += my_string[i]
    # return str
    list_str = list(my_string)
    list_str[num1], list_str[num2] = list_str[num2], list_str[num1]
    return ''.join(list_str)