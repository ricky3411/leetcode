class Solution:
    def firstUniqChar(self, s: str) -> int:

        dct = {}

        for chars in s:
            if chars not in dct:
                dct[chars] = 1
            else:
                dct[chars] += 1
        
        print(dct)

        for idx, letter in enumerate(s):
            if dct[letter] == 1:
                return idx
        
        return -1