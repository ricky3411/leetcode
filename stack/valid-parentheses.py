class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True

        map = {"}":"{", "]":"[", ")":"("}
        stack = []


        for i in s:
            if i in '([{':
                stack.append(i)
                print(stack)
            
            else:
                pop = stack.pop()
            
                if map[i] == pop:
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True