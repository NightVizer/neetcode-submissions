class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Решение с O(1) доп памяти, по времени O(n log n)
        return sorted(s) == sorted(t)
