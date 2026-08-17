class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        def create_hash(string):

            hash_map = {}

            for char in string:
                hash_map[char] = hash_map.get(char, 0) + 1

            return hash_map

        


        return create_hash(s) == create_hash(t)
        


        