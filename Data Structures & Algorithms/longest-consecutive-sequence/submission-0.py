class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        max_seq = 0

        for elem in nums:
            i = 1
            if elem - 1 not in nums:
                while elem + i in nums:
                    i += 1
            if i > max_seq:
                max_seq = i

        return max_seq
                


                



        