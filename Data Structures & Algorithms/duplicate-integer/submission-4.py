class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mapping = set()

        for n in nums:
            if n in mapping:
                return True
            mapping.add(n)

        return False