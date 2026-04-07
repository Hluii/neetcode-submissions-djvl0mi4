class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars1 = {}
        chars2 = {}
        for i in s:
            if i in chars1:
                chars1[i] += 1
            else:
                chars1[i] = 1
        for i in t:
            if i in chars2:
                chars2[i] += 1
            else:
                chars2[i] = 1
        if chars1 == chars2:
            return True
        else:
            return False