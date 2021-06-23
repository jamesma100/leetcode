class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = []
        for i in s:
            if i.isalnum():
                li.append(i.lower())
        return "".join(li) == "".join(li)[::-1]