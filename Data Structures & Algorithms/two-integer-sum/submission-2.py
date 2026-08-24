class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, v in enumerate(nums):
            seek = target - v
            if seek in seen:
                return sorted([i, seen[seek]])
            seen[v] = i
        