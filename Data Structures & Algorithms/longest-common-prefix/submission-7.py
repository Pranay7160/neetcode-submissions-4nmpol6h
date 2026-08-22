class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sm_str = strs[0]
        res = ""
        for s in strs:
            if len(s) < len(sm_str):
                sm_str = s
        
        i = len(sm_str)
        print("sm_str=>", sm_str)
        while len(sm_str) > 0:
            found = True
            for j in range(len(strs)):
                
                print("s[]=> ", sm_str[:i])
                print("j=> ", j)
                if strs[j][:i] != sm_str[:i]:
                    found = False
                    # sm_str = sm_str[:i]
                    i -= 1
                    break
            
            if found:
                return sm_str[:i]

                

        return sm_str
