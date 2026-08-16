class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for n in nums[:]:
            if n == val:
                nums.remove(val)
        
        return len(nums)