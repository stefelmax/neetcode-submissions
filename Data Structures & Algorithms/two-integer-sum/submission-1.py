class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dct = dict()

        for i, num in enumerate(nums):

            seek = target - num
            
            if seek in dct:
                return [i, dct[seek]] if i < dct[seek] else [dct[seek], i]

            dct[num] = i
        
        return False