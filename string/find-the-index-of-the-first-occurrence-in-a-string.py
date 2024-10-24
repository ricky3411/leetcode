class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        r = len(needle)

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:r] == needle:
                    return i
        return -1
