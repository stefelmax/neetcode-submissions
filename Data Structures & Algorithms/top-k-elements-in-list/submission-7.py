class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Create counter for each element
        frequencies = {}
        result = []

        # Count frequencies
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in frequencies.items():
            bucket[value].append(key)

        for i in range(len(bucket) - 1, 0, -1):
            for element in bucket[i]:
                result.append(element)

                if len(result) == k:
                    return result

          

        

        