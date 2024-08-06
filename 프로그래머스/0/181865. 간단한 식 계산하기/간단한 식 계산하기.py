def solution(binomial):
    each = binomial.split()
    if each[1] == "+":
        return int(each[0]) + int(each[2])
    elif each[1] == "-":
        return int(each[0]) - int(each[2])
    elif each[1] == "*":
        return int(each[0]) * int(each[2])