class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ''

        for s in strs:
            n = str(len(s))
            result += f'{n}#{s}'

        return result

    def decode(self, s: str) -> List[str]:
        
        result = []
        n = len(s)
        i = 0

        while i < n:
            j = i + 1
            while s[j] != '#':
                j += 1
            
            index_of_length = int(s[i:j])
            j = j + 1
            i = j + index_of_length
            substr = s[j:i]
            result.append(substr)
        
        return result





