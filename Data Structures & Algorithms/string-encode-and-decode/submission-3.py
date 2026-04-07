class Solution:

    def encode(self, strs: List[str]) -> str:
        # returns a str
        return_str= ""
        print(len(strs))
        for i,n in enumerate(strs):
            return_str += str(len(n)) + "#" + n
        print(return_str)
        return return_str
    def decode(self, s: str) -> List[str]:
        # returns a list of strs    
        return_list = []
        i = 0
        while i < len(s):
            j = s.find("#",i)
            print(j)
            length = int(s[i:j])
            print(length)
            string = s[j+1:j+1+length]
            print(string)
            return_list.append(string)
            i = length + j + 1
        return return_list

