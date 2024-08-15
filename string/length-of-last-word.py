class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # new = s.strip()
        # count = 0
        # rev = new[::-1]

        # for i in range(len(rev)):
        #     if rev[i].isalpha():
        #         count +=1
        #     else:
        #         break
        
        # return count

        count = 0
        letter = False

        for i in range(len(s)-1, -1, -1):
            if s[i].isspace():
                
                if letter:
                    break
            else:
                letter = True
                count +=1
                
        return count       