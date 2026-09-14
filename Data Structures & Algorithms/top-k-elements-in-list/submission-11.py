class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [[] for _ in range(len(nums) + 1)]
        counter = dict()
        need = list()

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for key, value in counter.items():
            bucket[value].append(key)

        for numbers in range(len(bucket)-1, 0, -1):
            for number in bucket[numbers]:
                need.append(number)
            
                if len(need) == k:
                    return need





        