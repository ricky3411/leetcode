class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        nlen = len(needle)
        s = 0
        check = 0

        for i, k in enumerate(haystack):
            if needle in haystack:
                return i
    
        return -1
