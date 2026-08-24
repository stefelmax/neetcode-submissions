class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for number, count in counter.items():
            bucket[count].append(number)

        result = []

        for i in range(len(bucket) -1, 0, -1):
            for element in bucket[i]:
                result.append(element)
                if len(result) == k:
                    return result

        



            