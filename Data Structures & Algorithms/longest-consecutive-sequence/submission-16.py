class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        h = set(nums)
        max_seq = 0

        for num in nums:
            i = 1

            if num - i not in h:

                while num + i in h:
                    i += 1
                max_seq = max(max_seq, i)

        return max_seq



        