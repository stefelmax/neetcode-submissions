class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        count = 0

        strs = sorted(strs)

        first, last = strs[0], strs[-1]

        n = len(strs[0])

        for i, char in enumerate(first):
            if char == last[i]:
                count += 1
            else:
                return first[:count]
        return first[:count]

            

            

            

            
        
