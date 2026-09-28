class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or len(t) == 0:
            return ""

        window_dict, t_dict = {}, {}
        
        t_dict = Counter(t)
        for key in t_dict:
            window_dict[key] = 0

        have, need = 0, len(t_dict)

        left_indx = 0
        res = [-1, -1]
        
        for right_indx in range(len(s)):
            letter = s[right_indx]
            window_dict[letter] = 1 + window_dict.get(letter, 0) 

            if window_dict[letter] == t_dict[letter]:
                have += 1

                while have == need:
                    if (res[0] ==-1 and res[1] == -1) or res[1]-res[0]+1 > right_indx-left_indx+1:
                        res = [left_indx, right_indx]

                    if s[left_indx] in window_dict:
                        window_dict[s[left_indx]] -= 1
                        if window_dict[s[left_indx]] < t_dict[s[left_indx]]:
                            have-=1
                    left_indx+=1
        
        return s[res[0]:res[1]+1]


