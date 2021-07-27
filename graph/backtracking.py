# Combinations
# Given n and k, return all possible combinations of k numbers out of range [1, n]
# May return in any order
def combine(n, k):
    def dfs(start, end, path, res):
        if len(path) == k:
            res.append(path)
            return
        if len(path) > k:
            return
        # already ordered, so no need to sort
        for i in range(start, end+1):
            dfs(i+1, end, path + [i], res)
    path, res = [], []
    dfs(1, n, path, res)
    return res

# Combination Sum
# Given array of distinct integers candidates and target, return all unique combinations
# of candidates where chosen numbers sum to target. Return in any order
# The same number may be chosen from candidates an unlimited number fo times
def combinationSum(candidates, target):
    def dfs(candidates, path, target, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        # use start index i to avoid duplicates, i.e. don't look back, only forward
        for i in range(len(candidates)):
            # not candidates[i+1:] because we want option of using candidates[i]
            # unlimited number of times
            dfs(candidates[i:], path+[candidates[i]], target-candidates[i], res)
    res, path = [], []
    dfs(candidates, path, target, res)
    return res

# Combination Sum II
# Given collection of numbers candidates and target, find all unique combinations in
# candidates where the candidate numbers sum to target. Each number may only be used
# once
# Numbers not distinct
def combinationSum2(candidates, target):
    def dfs(nums, path, target, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            dfs(nums[i+1:], path+[nums[i]], target-nums[i], res)
    path, res = [], []
    # sort and only look foward to eliminate duplicate paths
    candidates.sort()
    dfs(candidates, path, target, res)
    return res

# Combination Sum III
# Find all valid combinations of k numbers that sum up to n such that
# only 1-9 are used, each number used at most once
def combinatoinSum3(k, n):
    def dfs(start_num, target, path, res):
        if target < 0:
            return
        if len(path) > k:
            return
        if target == 0 and len(path) == k:
            res.append(path)
            return
        for i in range(start_num, 10):
            dfs(i+1, target-i, path+[i], res)
    res = []
    path = []
    start_num = 1
    dfs(start_num, n, path, res)
    return res


# Permutations
# Given array nums of distinct integers, return all possible permutations
def permute(nums):
    def dfs(nums, path, res):
        if len(path) == nums_len:
            res.append(path)
            return
        if len(path) > nums_len:
            return
        for num in nums:
            # no duplicates
            nums_copy = nums.copy()
            nums_copy.remove(num)
            dfs(nums_copy, path + [num], res)

    nums_len = len(nums) # save original length
    path, res = [], []
    dfs(nums, path, res)
    return res

# Permutations II
# Given a collection of numbers, nums that might contain duplicates, return all
# possible unique permutations in any order
# Numbers NOT distinct

def permuteUnique(nums):
    def dfs(nums, path, res):
        if len(path) == length:
            res.append(path)
            return
        if len(path) > length:
            return
        for i in range(len(nums)):
            # skip duplicate entries
            if i != 0 and nums[i] == nums[i-1]:
                continue
            copy = nums.copy()
            copy.remove(nums[i])
            dfs(copy, path + [nums[i]], res)































