class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        product = 1
        result = []

        for i in range(n):
            result.append(product)
            product *= nums[i]

        product = 1

        for i in range(n - 1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result

        