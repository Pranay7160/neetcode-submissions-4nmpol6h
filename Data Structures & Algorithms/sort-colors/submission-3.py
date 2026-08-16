class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_idx = 0
        two_idx = len(nums) - 1

        for n in nums[:]:
            if n == 0:
                nums[zero_idx] = 0
                zero_idx += 1
            elif n == 2:
                nums[two_idx] = 2
                two_idx -= 1
        

        for i in range(zero_idx, two_idx+1):
            nums[i] = 1

        

