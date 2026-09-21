class Solution:
    def trap(self, height: list[int]) -> int:

        # далее сделать подсчёт воды слева до ближайшего максимума и с права до ближайшего максимума

        # учесть отсутствие левого/правого проходов если максимум на крае.
        # учесть если столбов всего 1-2

        count_of_water = 0
        count_of_brick_walls = 0

        sorted_max_pillars_indxes = list()
        max_height = max(height)
        # найти точки максимума
        for indx in range(len(height)):
            if max_height == height[indx]:
                sorted_max_pillars_indxes.append(indx)

        # основная логика
        if len(sorted_max_pillars_indxes) > 1:
            # заполнить воду между точками максимумами если их больше 1
            # проверяем все пары столбов
            for left_indx in range(len(sorted_max_pillars_indxes) - 1):
                count_of_water += self.CountOfWaterInTwoPillars(sorted_max_pillars_indxes[left_indx],
                                                                sorted_max_pillars_indxes[left_indx+1], height)
            count_of_water += self.LeftCountOfWater(sorted_max_pillars_indxes[0], height)
            count_of_water += self.RightCountOfWater(sorted_max_pillars_indxes[len(sorted_max_pillars_indxes) - 1],
                                                     height)
            return count_of_water

        else:
            # левый правый проход
            # учесть отсутствие левого/правого проходов если максимум на крае.
            count_of_water += self.LeftCountOfWater(sorted_max_pillars_indxes[0], height)
            count_of_water += self.RightCountOfWater(sorted_max_pillars_indxes[len(sorted_max_pillars_indxes) - 1],
                                                     height)
            return count_of_water

    def CountOfWaterInTwoPillars(self, left_indx: int, right_indx: int, height: list[int]) -> int:
        count_of_brick_walls = 0
        for indx in range(left_indx + 1, right_indx):
            count_of_brick_walls += height[indx]

        return height[left_indx] * (right_indx - left_indx-1) - count_of_brick_walls

    def LeftCountOfWater(self, pillar_indx: int, height: list[int]) -> int:
        current_count_of_water = 0
        if (pillar_indx == 0 or pillar_indx == 1):
            return 0

        left_indx = self.MoveLeftPointerToFirstPool(0, pillar_indx, height)
        if left_indx == pillar_indx:
            return 0

        count_of_brick_walls = 0
        right_indx = left_indx + 1
        while True:
            if right_indx >= pillar_indx:
                return (height[left_indx] * (right_indx - left_indx-1) - count_of_brick_walls) + current_count_of_water

            if height[left_indx] >= height[right_indx]:
                count_of_brick_walls += height[right_indx]
                right_indx += 1
            else:
                current_count_of_water += height[left_indx] * (right_indx - left_indx-1) - count_of_brick_walls
                count_of_brick_walls = 0
                left_indx = self.MoveLeftPointerToFirstPool(right_indx, pillar_indx, height)
                if left_indx == pillar_indx:
                    return current_count_of_water
                right_indx = left_indx+1

    def RightCountOfWater(self, pillar_indx: int, height: list[int]) -> int:
        current_count_of_water = 0
        if (pillar_indx == len(height) - 1 or pillar_indx == len(height) - 2):
            return 0

        right_indx = self.MoveRightPointerToFirstPool(len(height) - 1, pillar_indx, height)
        if right_indx == pillar_indx:
            return 0

        count_of_brick_walls = 0
        left_indx = right_indx - 1
        while True:
            if right_indx <= pillar_indx:
                return (height[right_indx] * (right_indx - left_indx-1) - count_of_brick_walls) + current_count_of_water

            if height[right_indx] >= height[left_indx]:
                count_of_brick_walls += height[left_indx]
                left_indx -= 1
            else:
                current_count_of_water += height[right_indx] * (right_indx - left_indx-1) - count_of_brick_walls
                count_of_brick_walls = 0
                right_indx = self.MoveRightPointerToFirstPool(left_indx, pillar_indx, height)
                if right_indx == pillar_indx:
                    return current_count_of_water
                left_indx = right_indx - 1

    # в случае если нет басейнов возвращает pillar_indx
    def MoveLeftPointerToFirstPool(self, left_indx: int, pillar_indx: int, height: list[int]) -> int:
        while left_indx < pillar_indx:
            if height[left_indx] <= height[left_indx + 1]:
                left_indx += 1
            else:
                return left_indx
        return pillar_indx

    # в случае если нет басейнов возвращает pillar_indx
    def MoveRightPointerToFirstPool(self, right_indx: int, pillar_indx: int, height: list[int]) -> int:
        while right_indx > pillar_indx:
            if height[right_indx - 1] >= height[right_indx]:
                right_indx -= 1
            else:
                return right_indx
        return pillar_indx