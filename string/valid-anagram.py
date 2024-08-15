class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        word_s = {}
        word_t = {}

        for key, val in enumerate(s):
            if val not in word_s:
                word_s[val] = 1
            else:
                word_s[val] += 1

        for key, val in enumerate(t):
            if val not in word_t:
                word_t[val] = 1
            else:
                word_t[val] += 1
        
        return word_s == word_t