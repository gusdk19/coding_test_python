def solution(arr, n):
    new = []
    if len(arr) % 2:
        for i in range(len(arr)):
            new.append(arr[i] if i%2 else arr[i]+n)
    else:
        for i in range(len(arr)):
            new.append(arr[i]+n if i%2 else arr[i])
    return new