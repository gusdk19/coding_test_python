def solution(myString):
    str = ''
    for i in myString:
        str += i.lower()
    return str.replace('a', 'A')