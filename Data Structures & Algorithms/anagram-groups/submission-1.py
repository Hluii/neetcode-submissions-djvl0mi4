class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap with the sorted version of strings then the value is a list
        anaMap = {}
        for string in strs:
            sortedS = str(sorted(string))
            if sortedS in anaMap:
                # add to val
                anaMap[sortedS].append(string)
            else:
                # add to map
                anaMap[sortedS] = [string]
        return list(anaMap.values())
                