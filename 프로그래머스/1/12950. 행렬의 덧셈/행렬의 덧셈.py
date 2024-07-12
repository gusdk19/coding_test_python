def solution(arr1, arr2):
    result = []
    for k in range(len(arr1)):
        tmp = [i+j for i, j in zip(arr1[k], arr2[k])]
        result.append(tmp)
    return result