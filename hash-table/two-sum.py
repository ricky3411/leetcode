class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapping = {}

        for idx, val in enumerate(nums):

            diff = target - val

            if diff in mapping:
                return [idx, mapping[diff]]
            else:
                mapping[val] = idx

