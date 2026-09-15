class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^0-9a-zA-Z]", "", s.lower())
        print(s)

        left_indx = 0
        right_indx = len(s)-1
        while left_indx < right_indx:
            if s[left_indx] != s[right_indx]:
                return False
            
            left_indx+=1
            right_indx-=1
        
        return True