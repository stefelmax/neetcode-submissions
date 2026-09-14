class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_dict = defaultdict(list)

        for string in strs:
            mapping = [0] * 26

            for char in string:
                order = ord(char) - ord('a')
                mapping[order] += 1
            
            hash_dict[tuple(mapping)].append(string)

        return list(hash_dict.values())

