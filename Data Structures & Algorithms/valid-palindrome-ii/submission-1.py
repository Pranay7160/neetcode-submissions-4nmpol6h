class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                str1 = s[:left] + s[left + 1:]
                str2 = s[:right] + s[right + 1:]

                return str1 == str1[::-1] or str2[::-1] == str2
            
            left += 1
            right -= 1
        
        return True