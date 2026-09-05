class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for indx, value in enumerate(nums):
            diff = target-value
            if diff in memory:
                return [memory[diff],indx]
            memory[value] = indx
        
        return