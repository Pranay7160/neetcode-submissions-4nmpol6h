class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        dupnums = nums[:]
        for i in range(1, len(nums)):
            if dupnums[i] == dupnums[i-1]:
                nums.remove(dupnums[i-1])
        
        return len(nums)