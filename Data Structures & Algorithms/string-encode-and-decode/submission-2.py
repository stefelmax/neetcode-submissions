class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ''

        for string in strs:
            n = len(string)
            result += f'{n}#{string}'
        
        return result

    def decode(self, s: str) -> List[str]:

        i = 0
        n = len(s)
        result = []

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            number = int(s[i:j])
            i = j + 1
            j = i + number
            string = s[i:j] 
            result.append(s[i:j])
            i = j
        return result

            
