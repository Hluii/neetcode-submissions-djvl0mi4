class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init window, add char to set/list, move right, check, shrink left until char not in list
        if not s:
            return 0
        left, right = 0, 0
        window = set()
        count = 1
        while right < len(s):
            print("left: ", left, "Right: ", right)
            if s[right] not in window: window.add(s[right]) 
            else:
                while s[right] in window:
                    if s[left] == s[right]:
                        print("found")
                    window.remove(s[left])
                    left += 1
                window.add(s[right])
            count = max(count, len(window))
            print(count)
            right += 1
            print(window)
        print(right, left)
        return count
