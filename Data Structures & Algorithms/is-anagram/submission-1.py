class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Решение с O(1) доп памяти, по времени O(n log n)

        if len(s) != len(t):
            return False

        if sorted(s) == sorted(t):
            return True
        else:
            return False