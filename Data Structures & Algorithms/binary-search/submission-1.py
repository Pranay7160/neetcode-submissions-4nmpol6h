class Solution:
    def rec_search(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.rec_search(nums, target, left, mid - 1)
        elif nums[mid] < target:
            return self.rec_search(nums, target, mid + 1, right)


    def search(self, nums: List[int], target: int) -> int:
        return self.rec_search(nums, target, 0, len(nums) - 1)