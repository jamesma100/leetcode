# for each num, could be part of final result if 
#   negative * min (which is also negative)
#   if positive * max 
#   num itself
# store x, y separately because want to use old values to calculate cur_max, cur_min
# i.e. don't want to use updated cur max value to calculate the updated cur min value

def maxProduct(nums):
    cur_max, cur_min, imax = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        x = max(nums[i], cur_max*nums[i], cur_min*nums[i])
        y = min(nums[i], cur_min*nums[i], cur_max*nums[i])
        cur_max, cur_min = x, y
        imax = max(imax, cur_max)
    return imax