class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = dict()

        for i, value in enumerate(nums):
            seek = target - value

            if seek in seen:
                return sorted([i, seen[seek]])
            seen[value] = i