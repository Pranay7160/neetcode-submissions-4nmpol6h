class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for i, v in enumerate(nums):
            rem = target - v
            if rem in seen:
                return [nums.index(rem), i]
            
            seen.add(v)
        
        return None