class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dct = {}

        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in dct.items():
            bucket[value].append(key)

        result = []

        for count in range(len(bucket) - 1, 0, -1):
            for element in bucket[count]:
                result.append(element)
                if len(result) == k:
                    return result
