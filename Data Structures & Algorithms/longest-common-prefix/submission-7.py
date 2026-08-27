class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def check(string_1, string_2):

            i = 0
            while i < len(string_1) and i < len(string_2) and string_1[i] == string_2[i]:
                i += 1
            
            return string_1[:i]

        for string in set(strs):
            if 'common' not in locals():
                common = string
            common = check(common, string)

        return common

        