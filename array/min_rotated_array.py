# [4 5 6 7 0 1 2] rotated 4 times, min is 0


def findMin(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            return nums[i]
    return nums[0]