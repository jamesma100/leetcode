def search(nums, target):
    # binary search to find pivot, could also use solution for min sorted array problem
    l, r = 0, len(nums)-1
    while l < r:
        mid = (l+r) // 2
        if nums[mid] > nums[r]:
            l = mid+1
        else:
            r = mid
    piv = l
    l, r = 0, len(nums-1)
    # use <= because l==r could be target
    while l <= r:
        mid = (l+r) // 2                    # middle of array
        med = (mid+piv) % len(nums)         # middle of array if not rotated
        if nums[med] == target:
            return med
        elif nums[med] < target:
            l = mid+1
        else:
            r = mid-1
    return -1