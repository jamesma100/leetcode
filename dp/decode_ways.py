class Solution:
    # recursion w/ memoization
    def numDecodings1(self, s):
        def recurse(index):
            if index > len(s)-1:
                return 1
            # for one digit, any digit but 0 is possible
            if s[index] == "0":
                return 0
            if index == len(s)-1:
                return 1
            
            if index+1 not in memo:
                memo[index+1] = recurse(index+1)
            options = memo[index+1]
            if int(s[index:index+2]) <= 26:
                if index+2 not in memo:
                    memo[index+2] = recurse(index+2)
                options += memo[index+2]
            return options

        memo = {}
        return recurse(0)

























