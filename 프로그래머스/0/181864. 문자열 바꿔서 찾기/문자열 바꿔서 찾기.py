def solution(myString, pat):
    myString = myString.replace('A', 'b').replace('B', 'a')
    if pat.lower() in myString:
        return 1
    else:
        return 0