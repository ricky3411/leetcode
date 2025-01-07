class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        closeToOpen = {")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:

            #checking if it is a closing bracket: ),],}
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            
            #opening bracket        
            else:
                stack.append(c)
            
        return True if not stack else False