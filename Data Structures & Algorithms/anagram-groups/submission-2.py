class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dct = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            dct.setdefault(sorted_word, [])
            dct[sorted_word].append(word)

        return list(dct.values())
        