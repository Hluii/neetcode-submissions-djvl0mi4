class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # can hash or append to list dynamically by frequency
        freqHash = {}
        for num in nums:
            if num not in freqHash:
                freqHash[num] = 1
            else:
                freqHash[num] += 1
        print(freqHash)
        # swap key and value
        resHash = {}
        highest = 0
        res = []
        for num in set(nums):
            count = freqHash[num]
            if count not in resHash:
                resHash[count] = []
            resHash[count].append(num)
            highest = max(highest, count)
        print(resHash)
        while len(res) < k :
            if highest in resHash:
                while resHash[highest] != []:
                    res.append(resHash[highest].pop())
            highest -= 1
        return res

