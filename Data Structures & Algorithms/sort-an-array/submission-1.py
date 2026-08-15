class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        for i in range(ln):
            for j in range(i, ln):
                if nums[j] < nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        
        return nums