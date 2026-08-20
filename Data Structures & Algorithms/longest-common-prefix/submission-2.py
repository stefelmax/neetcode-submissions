class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        count = 0

        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        n = len(strs[0])

        while count < n and first[count] == last[count]:
            count += 1

        return first[:count]


            

            

            

            
        
