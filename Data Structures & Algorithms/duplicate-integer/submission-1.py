class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = set()

        for number in nums:
            if number in memory:
                return True
            
            memory.add(number)
        
        return False
        