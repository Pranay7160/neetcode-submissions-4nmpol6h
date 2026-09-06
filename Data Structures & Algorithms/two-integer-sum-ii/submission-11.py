class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last = len(numbers) - 1
        first = 0

        while last > first:
            total = numbers[last] + numbers[first]
            if target == total:
                return [first+1, last+1]
            if total > target:
                last -= 1
            else:
                first += 1
        
        return []
            