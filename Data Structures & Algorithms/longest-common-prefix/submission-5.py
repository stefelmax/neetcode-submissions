class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def common(a,b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1

            return a[:i]


        prefix = strs[0]

        for second in strs[1:]:
            prefix = common(prefix, second)
            if prefix == '':
                return ''
        return prefix
        