class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return len(s) == len(t) and set(s) == set(t)

        # mapS = {}
        # mapT = {}

        # for i in s:
        #     if i in mapS:
        #         mapS[i] += 1
        #     else:
        #         mapS[i] = 1
        
        # for i in t:
        #     if i in mapT:
        #         mapT[i] += 1
        #     else:
        #         mapT[i] = 1

        # return mapS == mapT
        

        