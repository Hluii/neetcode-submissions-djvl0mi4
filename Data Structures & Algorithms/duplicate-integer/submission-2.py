class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # make a set and compare len
        set_num = set(nums)
        return len(set_num) != len(nums)