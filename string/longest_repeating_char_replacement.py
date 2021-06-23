class Solution:
    def characterReplacement(self, s, k):
        l, r, imax = 0, 0, 0
        freq = [0] * 26     # tracks number of times each character appears
        max_freq = 0        # character that appears the most in current window
        while r < len(s):
            freq[ord(s[r])-ord('A')] += 1
            max_freq = max(max_freq, freq[ord(s[r])-ord('A')])
            while r-l+1-max_freq > k:   # length of window - max_freq is number of characters
                                        # we want to replace
                freq[ord(s[l])-ord('A')] -= 1  
                l += 1
            imax = max(imax, r-l+1)
        return imax
            
