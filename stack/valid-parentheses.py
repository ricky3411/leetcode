class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        map = {"(":")", "[":"]", "{":"}"}
        stack = []

        for c in s:
            if c in map:
                stack.append(c)
            
            else:
                #closing bracket
                if stack and c == map[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0 
                
        
