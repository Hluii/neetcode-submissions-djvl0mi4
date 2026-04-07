class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = nums.copy()
        mult = {} # key = index, value -> list to mult
        for i, n in enumerate(nums):
            mult[i] = nums[i+1:] + nums[:i]
            output[i] = math.prod(mult[i])

        return output