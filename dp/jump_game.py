class Solution:
    # use memoization: time limit exceeded ~ O(n^2)
    # recursive relation ar[i] -> possible to reach end from this position
    def canJumpDP(self, nums):
        ar = [False] * (len(nums)-1) + [True] # can reach last pos from last pos
        for i in range(len(nums)-2, -1, -1):
            # can reach end from i, instant True
            if i + nums[i] >= len(nums)-1:
                ar[i] = True
            # check further: if any ar[j] reacheable from i is True, set ar[i] = True
            else:
                for j in range(1,nums[i]+1):
                    if ar[i+j]:
                        ar[i] = True
                        break
        return ar[0] # answer = possible to reach end from beginning?

    # greedy solution
    # backwards
    # no need to store entire array
    # space O(1)
    # time O(n)
    def canJumpGreedy(self, nums):
        # define last_pos <- smallest index to reach end
        # if index i can reach last_pos, then possible to reach end from index i
        last_pos = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
    
    # greedy forward solution
    def canJumpForward(self, nums):
        imax = 0
        for i, num in enumerate(nums):
            if i > imax:
                return False
            imax = max(imax, i + num)
        return True

if __name__ == '__main__':
    print(Solution().canJumpDP([3,2,1,0,4])) # false
    print(Solution().canJumpDP([2,3,1,1,4])) # true

    print(Solution().canJumpGreedy([3,2,1,0,4])) # false
    print(Solution().canJumpGreedy([2,3,1,1,4])) # true
    