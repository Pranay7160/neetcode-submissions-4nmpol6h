class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ln = len(s)
        last = ln - 1
        first = 0

        while first < last:
            s[first], s[last] = s[last], s[first]
            last -= 1
            first += 1
        
        
        

        