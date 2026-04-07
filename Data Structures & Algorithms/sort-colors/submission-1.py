class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        pos_0 = 0
        pos_2 = l - 1

        for n in nums[:]:
            if n == 0:
                nums[pos_0] = 0
                pos_0 += 1
            elif n == 2:
                nums[pos_2] = 2
                pos_2 -= 1
        
        for j in range(pos_0, pos_2+1):
            nums[j] = 1
        