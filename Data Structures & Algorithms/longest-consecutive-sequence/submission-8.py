class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        h = set(nums)
        max_seq = 1

        for element in h:
            counter = 1
            if element - 1 not in h:
                
                while element + counter in h:
                    counter += 1
            max_seq = max(counter, max_seq)
        
        return max_seq


        