def bin_search(nums, val):
    def helper(nums, low, high):
        if high >= low:
            mid = (low + high) // 2
            if val == nums[mid]:
                return mid
            if val < nums[mid]:
                return helper(nums, low, mid-1)
            if val > nums[mid]:
                return helper(nums, mid+1, high)
        else:
            return -1

    return helper(nums, 0, len(nums)-1)


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print(bin_search(nums, 6))