class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        elems = set(nums)
        max_seq = 1

        for elem in elems:
            if elem - 1 not in elems:
                i = 1
                while elem + i in elems:
                    i += 1

                    max_seq = max(i, max_seq)

        return max_seq
