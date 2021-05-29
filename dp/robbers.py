# Recurrence relation: ar[i] = max(ar[i-2] + nums[i], ar[i-1])
# max(rob, no rob)

class Solution:
    # bottom up + memoization
    def rob_dp(self, nums):
        if len(nums) <= 2:
            return max(nums)
        ar = [0] * len(nums)
        ar[0] = nums[0]
        ar[1] = max(ar[0],nums[1])

        for i in range(2, len(nums)):
            ar[i] = max(nums[i]+ar[i-2], ar[i-1])
        return ar[-1]
    
    # top down + memoization
    def rob_dp2(self, nums):
        def rob_helper(i):
            if i < 0:
                return 0
            if mem[i] != -1:
                return mem[i]
            mem[i] = max(rob_helper(i-1), rob_helper(i-2) + nums[i])
            return mem[i]
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        mem = [-1 for _ in range(len(nums))]
        return rob_helper(len(nums)-1)
        
    def rob_greedy(self, nums):
        prev = cur = 0
        for num in nums:
            temp = prev     # store previous iteration's prev
            prev = cur      # current iteration's prev = last iteration's cur
            # update cur 
            cur = max(num+temp, prev) 
            print("temp: ", temp)
            print("prev: ", prev)
            print("cur: ", cur)
        return cur

if __name__ == '__main__':
    print(Solution().rob_greedy([1,2,3,1]))