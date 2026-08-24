
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dct = defaultdict(list)

        for string in strs:
            symbols = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                symbols[index] += 1

            t = tuple(symbols)
            dct[t].append(string)

        return list(dct.values())