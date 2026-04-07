from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        # .append(x) , x = .pop()
        # append until closing bracket I.E: ),],}
        # can do data validation by only appening opening brackets
        last = 0, '', ''
        for i, val in enumerate(s): # can turn this into for enumerate
            print(val)
            if val == '(' or val == '{' or val == '[':
                stack.append(val)
            if val == ')'or val == '}' or val == ']':
                if not stack:
                    return False
                last = stack.pop()   
                if val == ')' and last == '(':
                    continue
                elif val == '}' and last == '{':
                    continue
                elif val == ']' and last == '[':
                    continue
                else:
                    return False
                # case whe close andnot open? probably not bc it would be empty
        if stack:
            return False
        return True

                
