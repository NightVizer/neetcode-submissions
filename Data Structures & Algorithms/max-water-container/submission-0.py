class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_indx = 0
        right_indx = len(heights)-1
        max_capacity = min(heights[left_indx], heights[right_indx])* (right_indx-left_indx)

        while left_indx < right_indx:
            if (heights[left_indx] <= heights[right_indx]):
                # левый столб равен или меньше -> двигаем его
                new_left_indx = self.FindHigherPillarLeft(left_indx, heights) 
                if new_left_indx == -1:
                    # закончить алгоритм
                    return max_capacity
                else:
                    left_indx = new_left_indx
                    max_capacity = max(max_capacity, min(heights[left_indx], heights[right_indx])* (right_indx-left_indx))
            else:
                # если правый меньше -> двигаем его
                new_right_indx = self.FindHigherPillarRight(right_indx, heights) 
                if new_right_indx == -1:
                    # закончить алгоритм
                    return max_capacity
                else:
                    right_indx = new_right_indx
                    max_capacity = max(max_capacity, min(heights[left_indx], heights[right_indx])* (right_indx-left_indx))
        
        return max_capacity


    # в случае если нет столба выше, возвращает -1
    def FindHigherPillarLeft(self, left_indx:int, heights: List[int]) -> int:
        current_height = heights[left_indx]
        temp_left_indx = left_indx +1
        while True:
            if temp_left_indx > len(heights)-1:
                return -1
            if heights[temp_left_indx] <= current_height:
                temp_left_indx+=1
                continue
            
            return temp_left_indx
    
    def FindHigherPillarRight(self, right_indx:int, heights: List[int]) -> int:
        current_height = heights[right_indx]
        temp_right_indx = right_indx - 1
        while True:
            if temp_right_indx == 0:
                return -1
            if heights[temp_right_indx] <= current_height:
                temp_right_indx-=1
                continue
            
            return temp_right_indx