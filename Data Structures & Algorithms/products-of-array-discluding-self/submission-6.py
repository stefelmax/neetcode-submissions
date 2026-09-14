class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        result = []

        for i in nums:
            result.append(prefix)
            prefix *= i

        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= prefix
            prefix *= nums[i]

        return result


        