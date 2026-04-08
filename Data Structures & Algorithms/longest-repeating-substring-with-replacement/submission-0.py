class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniqueS = set(s)
        res = 0
        for c in uniqueS:
            left = count = 0
            for right in range(len(s)):

                if s[right] == c:
                    count += 1
                while right - left + 1 - count > k and left < right:
                    if s[left] == c:
                        count -= 1
                    left += 1
                res = max(res, right - left + 1)
        return res




        
