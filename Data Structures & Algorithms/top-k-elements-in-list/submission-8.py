class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dct = {}
        result = []

        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in dct.items():
            bucket[value].append(key)

        for i in range(len(bucket) - 1, 0, -1):
            for elem in bucket[i]:
                result.append(elem)

                if len(result) == k:
                    return result

        