class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 0]
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums[i+1:]:
                result[0] = i
                result[1] = nums.index(rem, i+1)
                return result
            
        
        return result