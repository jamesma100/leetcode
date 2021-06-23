class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        for i in t:
            if i not in dic:
                return False
            dic[i]-=1
            if dic[i] == 0:
                del dic[i]
        return dic=={}