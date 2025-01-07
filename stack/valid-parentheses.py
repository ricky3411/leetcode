class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True

        map = {"}":"{", "]":"[", ")":"("}
        stack = []


        for i in s:
            if i in '([{':
                stack.append(i)
            
            #closing bracket
            else:

                #checking if the stack is empty, if it is return false because it should not be since 
                #I just encountered a closing bracket that needs to match up with an opening one
                if not stack:
                    return False

                pop = stack.pop()
            
                if map[i] != pop:
                    return False
        
        return len(stack) == 0