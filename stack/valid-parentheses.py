class Solution:
    def isValid(self, s: str) -> bool:


        if len(s) == 0:
            return True

       # mapr = {")":"(", "]":"[", "}":"{"}

        map = {"(":")", "[":"]", "{":"}"}

        l = int(len(s)/2) -1
        r = int((len(s)-1)/2) +1

        if s[r] == map[s[l]]:
            l-=1
            r+=1
        else:
            return False 
        
        return True
            
