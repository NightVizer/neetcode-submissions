class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_indx = 0
        right_indx = len(s) - 1
        while left_indx < right_indx:
            while left_indx < right_indx and not self.alfanum(s[left_indx]):
                left_indx += 1
            while left_indx < right_indx and not self.alfanum(s[right_indx]):
                right_indx -= 1
            
            if s[left_indx].lower() != s[right_indx].lower():
                return False
            
            left_indx +=1
            right_indx -=1
                
        
        return True
        

    def alfanum(self, ch:str) -> bool:
        if (ord('A') <= ord(ch) <= ord('Z') or
            ord('a') <= ord(ch) <= ord('z') or
            ord('0') <= ord(ch) <= ord('9')):
            return True
        
        return False