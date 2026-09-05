class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v1, v2 = self.twoValues(nums, target)

        left_indx = 0
        right_indx = 0

        for temp_index in range(len(nums)):
            if v1 == nums[temp_index]:
                left_indx = temp_index
                break
        
        for temp_index in range(len(nums) - 1, -1, -1):
            if v2 == nums[temp_index]:
                right_indx = temp_index
                break

        if left_indx > right_indx:
            return [right_indx, left_indx]
        return [left_indx, right_indx]

    def twoValues(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)

        left_indx = 0
        right_indx = len(sortedNums)-1

        while left_indx < right_indx:
            if sortedNums[left_indx] + sortedNums[right_indx] == target:
                # Нужная комбинация
                return [sortedNums[left_indx], sortedNums[right_indx]]
            elif sortedNums[left_indx] + sortedNums[right_indx] < target:
                # Результат меньше цели
                left_indx +=1
            else:
                # Результат больше цели
                right_indx -=1