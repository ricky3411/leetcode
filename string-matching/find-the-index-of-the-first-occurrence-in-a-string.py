class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == "":
            return 0

        i = 0
        j = 0

        while i < len(haystack):
            n_ptr = 0
            j = i  # Update j to be equal to i

            # Check if we can match the needle starting at index i in the haystack
            while j < len(haystack) and n_ptr < len(needle) and haystack[j] == needle[n_ptr]:
                j += 1
                n_ptr += 1

            # If we've matched the entire needle
            if n_ptr == len(needle):
                return i

            i += 1 

        return -1

    
        # if needle == "":
        #     return 0

        # for i in range(len(haystack)+1-len(needle)):
        #     if haystack[i: i+len(needle)] == needle:
        #         return i
        # return -1