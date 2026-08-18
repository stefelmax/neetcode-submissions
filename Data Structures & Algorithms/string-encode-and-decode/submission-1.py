class Solution:
    def __init__(self):
        self.dct = dict()

    def encode(self, strs: List[str]) -> str:

        result = ''

        for i, string in enumerate(strs):
            result += str(i) + '#'
            self.dct[i] = string

        return result


    def decode(self, s: str) -> List[str]:

        nums = s.rsplit('#')[:-1]
        result = []
        for num in nums:
            result.append(self.dct[int(num)])
    
        return result