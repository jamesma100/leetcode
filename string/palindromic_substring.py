class Solution:
    def longestPalindrome(s):
        is_pal = [[False for i in range(len(s))] for j in range(len(s))]
        imax, res = 1, s[0]
        # base case 1: 1 letter
        for i in range(len(s)):
            is_pal[i][i] = True
        # base case: 2 letter
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                is_pal[i-1][i] = True
        # build on base cases
        # if s[i] == s[j] and is_pal[i+1][j-1] then set is_pal[i][j]
        for end in range(1, len(s)):
            for start in range(end):
                if s[end] == s[start] and (is_pal[start+1][end-1] or end == start+1):
                    is_pal[start][end] = True
                    if end-start+1 > imax:
                        imax = end-start+1
                        res = s[start:end+1]
        return res