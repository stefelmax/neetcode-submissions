class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        result = [1] * n
        multiple = 1

        for i in range(n):
            result[i] = multiple
            multiple *= nums[i]

        multiple = 1

        for i in range(n - 1, -1, -1):
            result[i] *= multiple
            multiple *= nums[i]

        return result





        