class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort both, then compare
        print(sorted(s))
        return sorted(s) == sorted(t)