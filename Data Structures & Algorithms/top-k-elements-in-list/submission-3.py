class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        pq = []
        result = list()
        for value in counts.keys():
            heapq.heappush(pq, (-counts[value], value))

        for _ in range(k):
            result.append(heapq.heappop(pq)[1])

        return result
