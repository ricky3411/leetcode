class Solution:
    def isValid(self, s: str) -> bool:


        if len(s) == 0:
            return True
        
        if len(s) == 1:
            return False

       # mapr = {")":"(", "]":"[", "}":"{"}

        map = {"(":")", "[":"]", "{":"}"}

        l = int(len(s)/2) -1
        r = int((len(s)-1)/2) +1

        if l >= 0 and r <= len(s):
            if s[l] in map and s[r] == map[s[l]]:
                l-=1
                r+=1
            else:
                return False 
            
        return True