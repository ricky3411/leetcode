class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last = 0

        for i in range(1,len(nums)):
            if nums[i] != 0:
                temp = nums[last]
                nums[last] = nums[i]
                nums[i] = temp
                
                last += 1