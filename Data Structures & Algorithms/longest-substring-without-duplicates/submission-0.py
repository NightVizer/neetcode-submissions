class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()

        # учесть когда длинна 0 и 1
        if len(s) ==0:
            return 0
        elif len(s) ==1:
            return 1

        left_indx, right_indx = 0, 1
        max_len = 1

        # двигаемся до первой различной комбинации
        while s[left_indx] == s[right_indx]:
            left_indx += 1
            right_indx += 1

            if right_indx > len(s)-1:
                return max_len
        
        letters.add(s[left_indx])
        letters.add(s[right_indx])
        max_len = 2

        while right_indx < len(s):
            right_indx+= 1
            if right_indx >= len(s):
                return max(max_len, len(letters))
            if s[right_indx] in letters:
                max_len = max(max_len, len(letters))
                while True:
                    letters.remove(s[left_indx])
                    if s[left_indx] == s[right_indx]:
                        left_indx+=1
                        letters.add(s[right_indx])
                        break
                    left_indx+=1
            else:
                letters.add(s[right_indx])

        return max_len

