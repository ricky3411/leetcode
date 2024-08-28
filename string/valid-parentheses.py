class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True

        map = {"}":"{", "]":"[", ")":"("}
        stack = []


        for i in s:
            if i in '([{':
                stack.append(i)
            
            else:

                if not stack:
                    return False

                pop = stack.pop()
            
                if map[i] != pop:
                    return False
        
        return len(stack) == 0