class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        bucket = [1 for _ in range(len(nums))]
        multi = 1

        for i in range(len(nums)):
            bucket[i] *= multi
            multi *= nums[i]

        multi = 1

        for i in range(len(nums) -1, -1, -1):
            bucket[i] *= multi
            multi *= nums[i]

        return bucket






        