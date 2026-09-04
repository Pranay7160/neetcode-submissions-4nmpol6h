class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # not done by me, for the sake of streak, i am going to revisit this Question
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest