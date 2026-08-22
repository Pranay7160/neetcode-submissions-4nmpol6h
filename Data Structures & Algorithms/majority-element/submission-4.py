class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # This is Boyer–Moore Majority Vote, and your implementation 
        # is the standard O(n) time    / O(1) space solution.
        candidate = nums[0]
        count = 0

        for n in nums:
            if count == 0:
                candidate = n
            
            if candidate == n:
                count += 1
            else:
                count -= 1
        
        return candidate
        