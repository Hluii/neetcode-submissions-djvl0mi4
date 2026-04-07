class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash map
        # key -> num val -> count
        # iterate through array
        # return false if count > 1
        # else True
        num_dict = {}
        for i, n in enumerate(nums):
            if n in num_dict:
                return True
            else:
                num_dict[n] = 1
        return False
        