class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dct = set()
        for num in nums:
            if num in dct:
                return True
            else:
                dct.add(num)

        return False