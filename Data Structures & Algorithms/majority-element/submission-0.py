class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dct = {}

        for i, num in enumerate(nums):
            dct[num] = dct.get(num, 0) + 1

        return sorted(dct.items(), key=lambda x: x[1], reverse=True)[0][0]
        
