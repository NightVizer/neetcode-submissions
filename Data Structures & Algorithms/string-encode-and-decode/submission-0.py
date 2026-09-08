class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + '#' + word
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            lenNumber = 0
            # считаем разделитель
            resultNumberInString = ""
            while s[i] != '#':
                resultNumberInString += s[i]
                i+=1
            
            lenNumber = int(resultNumberInString)

            # чтобы знак "#" пропустить
            i+=1
            
            oneWord = ""
            while lenNumber > 0:
                oneWord+= s[i]
                lenNumber-=1
                i+=1

            result.append(oneWord)
        
        return result
            

    def readLen(self, i: int, s: str) -> int:
        resultNumberInString = ""
        while s[i] != '#':
            resultNumberInString += s[i]
            i+=1
        
        return int(resultNumberInString)
