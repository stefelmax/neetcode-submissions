class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''

        for string in strs:
            result += f'{len(string)}#{string}'

        return result

    def decode(self, s: str) -> List[str]:
        
        if s == '':
            return []

        result = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            size = int(s[i:j])
            start = j + 1
            i = start + size
            sub_str = s[start:i]
            result.append(sub_str)

        return result




        