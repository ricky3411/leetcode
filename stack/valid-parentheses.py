class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True
        
        if len(s) == 1:
            return False

        map = {"}":"{", "]":"[", ")":"("}
        stack = []


        for i in s:
            if i in '([{':
                stack.append(i)
            
            else:

                if stack: 
                    pop = stack.pop()
            
                    if map[i] == pop:
                        continue
                    else:
                        return False
        
        if len(stack) == 0:
            return True