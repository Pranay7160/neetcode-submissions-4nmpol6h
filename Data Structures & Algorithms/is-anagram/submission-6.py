class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr = [0] * 26
        ord_a = ord('a')
        for i in range(len(s)):
            arr[ord(s[i]) - ord_a] += 1
            arr[ord(t[i]) - ord_a] -= 1
        
        for check in arr:
            if check != 0:
                return False
        
        return True

        