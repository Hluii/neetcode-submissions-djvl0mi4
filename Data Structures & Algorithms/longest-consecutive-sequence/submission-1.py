class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        print(set_nums)
        sorted_set = sorted(set_nums)
        print(sorted_set)
        seq_list = []
        con_seq = {}
        highest, counter, longest = 0,0,0
        print(sorted_set)
        for i in sorted_set:
            if i > highest + 1:
                con_seq[counter] = seq_list
                seq_list = []
                seq_list.append(i)
                counter = 1
            else:
                counter += 1    
            highest = i  
            if counter > longest:
                longest = counter  
        return longest
