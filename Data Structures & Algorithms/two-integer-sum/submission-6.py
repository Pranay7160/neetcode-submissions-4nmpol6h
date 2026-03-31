class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 0]
        for i, val in enumerate(nums):
            rem = target - val
            if rem in nums[i+1:]:
                rem_i = nums.index(rem, i+1)
                result[0] = i
                result[1] = rem_i
                return result
        
        return result
