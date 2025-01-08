class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == "":
            return True 

        newS = []

        for c in s:
            if c.isalnum():
                newS.append(c.lower())

        print(newS)

        newS = ''.join(newS)
        
        return newS == newS[::-1]
            
        




        