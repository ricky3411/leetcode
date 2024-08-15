class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        freq = {}
        maxFreq = 0
        count = 0

        for num in nums:
            if num in freq:
                freq[num] += 1
            else: 
                freq[num] = 1

            maxFreq = max(freq[num], maxFreq)

        for val in freq.values():
            if val == maxFreq:
                count += val
        
        return count