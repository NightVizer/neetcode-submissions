class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for x in range(len(nums))]
        postfix = [1 for x in range(len(nums))]

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        postfix[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        
        result = []
        result.append(postfix[1])
        for i in range(1, len(nums) - 1):
            result.append(prefix[i-1] * postfix[i+1])
        result.append(prefix[len(nums)-2])

        return result