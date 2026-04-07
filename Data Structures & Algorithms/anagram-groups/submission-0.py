class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # copy list
        sort_strs = strs
        # intialize hashmap
        sorted_ana = {}
        # iterate through copy list
        for i, n  in enumerate(sort_strs):
            n = "".join(sorted(n))
            # sort each string, [aa,cc,bb,aa,cc]
            if n not in sorted_ana: sorted_ana[n] = []
            sorted_ana[n].append(strs[i])
            # add string as key and index as value
        return list(sorted_ana.values())