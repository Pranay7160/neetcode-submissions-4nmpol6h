class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for i in nums:
            if (i-1) not in nums:
                y = i + 1
                while y in nums:
                    y += 1 
                longest = max(longest, y - i) 
        
        return longest

        