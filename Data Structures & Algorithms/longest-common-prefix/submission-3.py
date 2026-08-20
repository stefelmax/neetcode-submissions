class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs = sorted(strs)
        i = 0

        while i < len(strs[0]) and strs[0][i] == strs[-1][i]:
            i += 1

        return strs[0][:i]


            

            

            

            
        
