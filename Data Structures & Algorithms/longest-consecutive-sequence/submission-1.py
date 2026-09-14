import heapq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        pq = []
        for number in set(nums):
            heapq.heappush(pq, number)

        last_value = float("-inf")
        max_count = 1
        current_count = 1
        while len(pq) > 0:
            current_value = heapq.heappop(pq)
            if last_value == float("-inf"):
                last_value = current_value
                current_count = 1
                continue
            elif last_value+1 != current_value:
                max_count = max(current_count, max_count)
                last_value = current_value
                current_count = 1
            else:
                last_value = current_value
                current_count += 1
        
        max_count = max(current_count, max_count)

        return max_count