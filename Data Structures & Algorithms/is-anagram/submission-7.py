class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        def create_vector(string):

            vector = [0] * 26

            for char in string:
            
                ascii_code = ord(char) - ord('a')
                vector[ascii_code] += 1 

            return vector

        return create_vector(s) == create_vector(t)
        


        