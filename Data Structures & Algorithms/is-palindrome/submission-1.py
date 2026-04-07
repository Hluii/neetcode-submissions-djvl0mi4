import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        replace_list = ["'","?",",",".","!",","]
        translator = str.maketrans('','',string.punctuation)
        s = s.translate(translator)
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            print(s[left] + s[right])
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
            

        