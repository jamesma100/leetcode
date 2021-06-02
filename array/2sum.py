# return indices of two numbers that add up to target
# 
def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        dic[target-num] = i
    for i, num in enumerate(nums):
        if num in dic and i != dic[num]: # ensure no duplicates
            return [i, dic[num]]