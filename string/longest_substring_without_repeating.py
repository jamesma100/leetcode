class Solution:
    def lengthOfLongestSubstring(self, s):
        l, r, imax = 0, 0, 0
        exists = {}     # whether character exists in current window
        while r < len(s):
            if ord(s[r]) not in exists or not exists[ord(s[r])]:
                exists[ord(s[r])] = True
            else:       # character at r exists in window
                while exists[ord(s[r])]:
                    exists[ord(s[l])] = False
                    l += 1
                exists[ord(s[r])] = True
            imax = max(imax, r-l+1)
            r += 1
        return max