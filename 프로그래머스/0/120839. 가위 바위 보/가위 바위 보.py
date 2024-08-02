def solution(rsp):
    str = ''
    win = {'2': '0', '0': '5', '5': '2'}
    for i in rsp:
        str += win[i]
    return str