class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_indx = 0
        right_indx = len(numbers)-1

        while left_indx < right_indx:
            if numbers[left_indx]+numbers[right_indx] < target:
                left_indx+=1
            elif numbers[left_indx]+numbers[right_indx] > target:
                right_indx-=1
            else:
                return [left_indx+1,right_indx+1]
        
        # недостежимо 
        return [0,0]