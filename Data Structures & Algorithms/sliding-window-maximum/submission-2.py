from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()

        left_indx = 0
        right_indx = 0
        for indx in range(k):
            if len(q) == 0:
                q.append(nums[indx])
                continue
            if q[-1] < nums[indx]:
                while True:
                    if len(q) == 0 or q[-1] >= nums[indx]:
                        break
                    q.pop()

            q.append(nums[indx])

        right_indx = k - 1

        result = list()
        result.append(q[0])
        while right_indx < len(nums) - 1:
            if q[0] == nums[left_indx]:
                q.popleft()

            left_indx += 1
            right_indx += 1
            if len(q) == 0:
                pass
            elif q[-1] < nums[right_indx]:
                while True:
                    if len(q) == 0 or q[-1] >= nums[right_indx]:
                        break
                    q.pop()

            q.append(nums[right_indx])

            result.append(q[0])

        return result