class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        return map(int,(",".join(str(int("".join(map(str,digits)))+1))).split(","))

