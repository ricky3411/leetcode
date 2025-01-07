class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        newList = []  # This will store pairs of (value, index)

        for idx, val in enumerate(nums):
            diff = target - val  # Calculate the difference

            # Check if the difference exists in the stored list
            for stored_val, stored_idx in newList:
                if stored_val == diff:
                    return [stored_idx, idx]  # Return the indices of the pair

            # Append the current value and its index to the list
            newList.append((val, idx))