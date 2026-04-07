class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hash map of compliments 
        comps = {}
        # iterate through target and add compiment to map 
        for i,num in enumerate(nums):
            comp = target - num
            if num in comps:
                return [comps[num], i]
            if comp not in comps:
                comps[comp] = i 
        

        


