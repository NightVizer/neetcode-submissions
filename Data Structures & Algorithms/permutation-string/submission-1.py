class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) >len(s2):
            return False

        s1_letters = {}
        for letter in s1:
            s1_letters[letter] = 1 + s1_letters.get(letter, 0)
        current_letters = {}

        left_indx = 0
        right_indx = len(s1) - 1

        indx = 0
        while indx <= right_indx:
            current_letters[s2[indx]] = 1 + current_letters.get(s2[indx], 0)
            indx += 1
        
        if s1_letters == current_letters:
            return True

        # основная логика проверки + перемещения окна
        while right_indx < len(s2):
            # возможно добавить проверку на right_indx+1
            if right_indx +1 >= len(s2):
                # завершаемся
                return False
            
            right_indx+=1
            current_letters[s2[right_indx]] = 1+ current_letters.get(s2[right_indx], 0)

            current_letters[s2[left_indx]] -= 1
            if current_letters[s2[left_indx]] == 0:
                current_letters.pop(s2[left_indx])
            left_indx+=1

            if s1_letters == current_letters:
                return True
            
        
        return False

