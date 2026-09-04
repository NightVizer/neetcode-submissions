class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()

        for letter in s:
            if letter in letters: 
                letters[letter] += 1
            else: 
                letters[letter] = 1

        for letter in t:
            if (letters.get(letter,0) >0):
                letters[letter] -=1
            else:
                return False
        
        for value in letters.values():
            if (value > 0):
                return False
            
        return True