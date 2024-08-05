def solution(nums):
    num = {}
    for i in nums:
        num[i] = 1
    
    max_num = len(nums)//2
    if len(num.keys()) >= max_num:
        return max_num
    else:
        return len(num.keys())