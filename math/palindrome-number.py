class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0 or x % 10 == 0 and x != 0:
            return False

        rev = 0

        chopped = x

        while chopped > 0:

            rem = chopped % 10

            rev = rev * 10 + rem

            chopped = chopped//10

        if rev == x:
            return True
        return False

        