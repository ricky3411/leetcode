class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # nlen = len(needle)
        # s = 0
        # check = 0

        # for i in range(len(haystack)):
        #     if haystack[i] == needle[s]:
        #         check = i

        # return -1

        l = 0
        r = len(needle)
       # check = 0

        print(len(haystack))

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
              #  check = i
                if haystack[i:r+i] == needle:
                    return i
        return -1
