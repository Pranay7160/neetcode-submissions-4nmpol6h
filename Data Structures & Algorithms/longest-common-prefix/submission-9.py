class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        sm_str = min(strs, key=len)
        i = len(sm_str)
        while len(sm_str) > 0:
            for s in strs:
                if s[:i] != sm_str[:i]:
                    i -= 1
                    sm_str = sm_str[:i]
                    break
            else:
                return sm_str

        return sm_str
