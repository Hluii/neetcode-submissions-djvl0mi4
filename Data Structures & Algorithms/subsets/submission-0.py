class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        # add the number to each set if it doesnt exist
        for num in nums:
            Nsets = [curr + [num] for curr in res]
        
            res.extend(Nsets)

        return res
