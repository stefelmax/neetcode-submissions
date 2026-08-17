class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dct = {}

        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        return [element[0] for element in sorted(dct.items(), key=lambda x: x[1], reverse=True)[:k]]

        