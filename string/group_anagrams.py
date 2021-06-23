from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            ar = [0] * 26
            for l in s:
                ar[ord(l)-ord('a')]+=1
            hmap[tuple(ar)].append(s)
        return hmap.values()
        