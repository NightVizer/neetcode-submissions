class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for word in strs:
            keyOfNewWord = self.getStringKey(word)
            if keyOfNewWord in groups:
                groups[keyOfNewWord].append(word)
            else:
                groups[keyOfNewWord] = [word]

        resultList = list()

        for value in groups.values():
            resultList.append(value)

        return resultList

    def getStringKey(self, word: str) -> str:
        word = "".join(sorted(word))

        if len(word) == 0:
            return ""
        resultString = ""
        indx = 0
        while True:
            startLetter = word[indx]
            counterOfLetters = 1
            while True:
                if indx + 1 >= len(word):
                    resultString += str(counterOfLetters) + startLetter
                    return resultString
                if word[indx + 1] != startLetter:
                    break
                counterOfLetters += 1
                indx += 1

            resultString += str(counterOfLetters) + startLetter
            indx += 1

            if indx >= len(word):
                return resultString
