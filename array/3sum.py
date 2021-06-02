def threeSum(nums):
    # window algorithm
    # sort array, loop through all triplets, maintain window
    # i iterates from 0 to len(nums)-2
    # shift/resize window (nums[l] to nums[r]) until nums[i] + nums[l] + nums[r] == 0
    # optimize by skipping duplicate nums[i] in for loop
    # optimize by skipping duplicate nums[l] and nums[r] in while loop
    '''
    | -4 | -1 | -1 | 0 | 1 | 2 |
      i     l                r

    '''
    nums.sort()
    trips = []
    for i in range(0, len(nums)-2):
        # skip identical iteration if nums[i] has been visited
        if i > 0 and nums[i]==nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            tmp = nums[i]+nums[l]+nums[r]
            if tmp == 0:
                trips.append(tuple(sorted([nums[i],nums[l],nums[r]])))
                # skip identical iteration if nums[l] already visited
                while nums[l]==nums[l+1] and l+1<r:
                    l+=1
                # skip identical iteration if nums[r] already visited
                while nums[r]==nums[r-1] and l<r:
                    r-=1
                l+=1
                r-=1
            elif tmp < 0:
                l+=1
            else:
                r-=1
    return trips
