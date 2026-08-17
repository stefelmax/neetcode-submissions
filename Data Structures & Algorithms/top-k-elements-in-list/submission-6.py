class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            return [nums[0]]

        dct = {}

        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        return [element[0] for element in sorted(dct.items(), key=lambda x: x[1], reverse=True)[:k]]

        