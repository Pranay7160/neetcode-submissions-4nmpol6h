class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [0, 0]
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums[i+1:]:
                ans[0] = i
                ans[1] = nums.index(rem, i+1)
                return ans

        