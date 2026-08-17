class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dct = {}

        for word in strs:
            vector = [0] * 26
            for char in word:
                ascii = ord(char) - ord('a')
                vector[ascii] += 1
                tuple_vector = tuple(vector)
            
            if word == "":
                tuple_vector = None

            dct.setdefault(tuple_vector, [])
            dct[tuple_vector].append(word)

        return list(dct.values())



        