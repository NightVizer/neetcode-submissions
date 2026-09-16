class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)

        hashmap = dict()
        for value in sorted_nums:
            hashmap[value] = hashmap.get(value, 0) + 1

        result = set()
        for first_value_indx in range(len(sorted_nums)):
            for second_value_indx in range(first_value_indx + 1, len(sorted_nums)):
                if self.CanAddValue(sorted_nums[first_value_indx], sorted_nums[second_value_indx], hashmap):
                    triplet = [sorted_nums[first_value_indx], sorted_nums[second_value_indx],
                               -(sorted_nums[first_value_indx] + sorted_nums[second_value_indx])]
                    result.add(tuple(sorted(triplet)))

        return [list(triplet) for triplet in result]

    def CanAddValue(self, value1: int, value2: int, hashmap: dict) -> bool:
        ost = -(value1 + value2)
        if ost in hashmap:
            countOfValue = hashmap[ost]
            if countOfValue >= 3:
                return True
            else:
                count_of_equal = 1
                if value1 == ost:
                    count_of_equal += 1
                if value2 == ost:
                    count_of_equal += 1

                if count_of_equal > hashmap[ost]:
                    return False
                else:
                    return True

        return False