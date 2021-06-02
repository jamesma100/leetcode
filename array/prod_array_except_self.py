# answer[i] is product of all elements of nums except nums[i]
# first pass: for each i, store product of all num[j] for all j left of i
# second pass: for each i, multiply stored results by all num[j] for j right of i

class Solution:
    def productExceptSelf(self, nums):
        prod = [1 for _ in range(len(nums))]
        l, r = 1, 1
        for i in range(len(nums)):
            prod[i] *= l
            l *= nums[i]
        for j in range(len(nums)):
            prod[-1-j] *= r
            r *= nums[-1-j]
        return prod