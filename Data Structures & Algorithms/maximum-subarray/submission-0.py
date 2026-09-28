class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            res = max(res, current)
        return res
            



        
        