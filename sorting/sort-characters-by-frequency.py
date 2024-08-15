class Solution:
    def frequencySort(self, s: str) -> str:

        #iterate through the string 
        #counter the frequency of the letters 
        #whatever value is the most, print out that value by * by the frequency 

        mp = {}
        r = ""

        for key, val in enumerate(s):

            if val not in mp:
                mp[val] = 1
            else:
                mp[val] += 1

        sorted_mp = dict(sorted(mp.items(), key=lambda x: x[1], reverse=True))

        for key, value in sorted_mp.items():
            r += key * value
        
        return r
