class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strings = sorted(strs)

        counter = 0

        for i in range(len(strings[0])):
            if strings[0][i] != strings[-1][i]:
                break
            counter += 1

        return strings[0][:counter]
        