class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 1:
            return True
 
        no = s.lower()
        check = []

        for i in range(len(s)):
            if no[i].isalnum():
                check.append(no[i])
        
        back = []

        for j in range(len(check)-1,-1,-1):
            back.append(check[j])

        return "".join(check) == "".join(back)