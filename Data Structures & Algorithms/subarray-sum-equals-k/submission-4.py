class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = { 0 : 1 }
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            needed_total = prefix_sum - k
            count += prefix_sum_count.get(needed_total, 0)

            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

        
        return count

        