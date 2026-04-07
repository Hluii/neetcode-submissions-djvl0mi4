class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        index = {}
        for i in nums:
            if i in index:
                return True
            else:
                index[i]= 1
        return False  
        