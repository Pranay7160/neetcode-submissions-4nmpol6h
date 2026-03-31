class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_c = Counter(s)
        t_c = Counter(t)

        for key in s_c:
            if s_c[key] != t_c[key]:
                return False
        
        return True


        