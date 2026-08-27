class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ''

        result = ''

        for string in strs:
            counter = str(len(string))
            result += f'{counter}#{string}'

        return result

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            
            word_length = int(s[i:j]) # 0 1
            start = j + 1
            i = start + word_length
            word = s[start:i]
            result.append(word)
        return result



4 # p o r t





