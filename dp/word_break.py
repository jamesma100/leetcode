# given string s and dictionary of strings wordDict check if s can be segmented into
# space separated sequence of one or more dictionary words

class Solution:
    def word_break(self, s, wordDict):
        # dp[i] means entire string up to i can be made up of words in wordDict
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if i+1 < len(word):
                    continue
                # find matching word ending at i
                if s[i-len(word)+1:i+1] == word:
                    # mark True if string so far only has current word OR
                    # string scanned is longer than current word so check if 
                    # previous iteration of problem is true
                    if i-len(word)+1 == 0 or dp[i-len(word)]:
                        dp[i] = True
        return dp[-1]

if __name__ == '__main__':
    if not Solution().word_break("pianophone", ["piano","phone"]):
            print("test 1 failed")
    else:
        print("test 1 passed")

    if Solution().word_break("rambo", ["brrr"]):
            print("test 2 failed")
    else:
        print("test 2 passed")

    if not Solution().word_break("hormonemonsterroar", ["hormone","roar","monster"]):
            print("test 3 failed")
    else:
        print("test 3 passed")

    if Solution().word_break("kimchsushi", ["kimchi","suchi"]):
            print("test 4 failed")
    else:
        print("test 4 passed")
