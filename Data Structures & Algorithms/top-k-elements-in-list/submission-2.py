class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        pq = []
        nums = sorted(nums)

        i = 0
        while i < len(nums):
            currentValue = nums[i]
            counter = 1

            while True:
                if i + 1 >= len(nums):
                    heapq.heappush(pq, (-counter, currentValue))
                    i += 1
                    break

                if nums[i + 1] == currentValue:
                    counter += 1
                    i += 1
                else:
                    heapq.heappush(pq, (-counter, currentValue))
                    i += 1
                    break

        result = list()
        for _ in range(k):
            result.append(heapq.heappop(pq)[1])

        return result
