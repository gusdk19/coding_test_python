def solution(my_string):
    new_string = ''
    for i in my_string:
        if i.islower():
            new_string = new_string + i.upper()
        else:
            new_string = new_string + i.lower()
    return new_string