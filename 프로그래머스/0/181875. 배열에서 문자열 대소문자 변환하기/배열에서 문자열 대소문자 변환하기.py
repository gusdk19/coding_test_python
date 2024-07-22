def solution(strArr):
    str = []
    for i in range(len(strArr)):
        if i % 2 == 1:
            str.append(strArr[i].upper())
        else:
            str.append(strArr[i].lower())
    return str