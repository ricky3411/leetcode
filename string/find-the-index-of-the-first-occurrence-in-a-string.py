class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

       # for i in range(len(haystack))

       for i in range(len(haystack)):
            if needle in haystack:
                return i
       return -1        