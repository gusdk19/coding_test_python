def solution(s):
    answer = False
    # 문자열 s의 길이가 4 혹은 6
    # 숫자로만 구성되어 있어야 함
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            answer = True
    return answer