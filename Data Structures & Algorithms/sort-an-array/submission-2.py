class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ln = len(nums)

        for i in range(ln):
            for j in range(0, ln - i - 1):
                if nums[j+1] < nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        return nums