# find contiguous subarray containing at least one number which has largest sum and return it

def maxSubarray(nums):
    cur = 0
    imax = nums[0]
    for i, num in enumerate(nums):
        cur = max(num, cur+num) # decide to keep adding to cur or start over (set cur to num)
        imax = max(imax, cur)
    return imax