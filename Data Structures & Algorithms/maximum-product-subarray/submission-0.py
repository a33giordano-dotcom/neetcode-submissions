class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = nums[0]
        max_dp = nums[0] 
        min_dp = nums[0]

        for i in range(1, len(nums)):

            current = nums[i]
            new_max= max(current, max_dp * current, min_dp * current)
            new_min = min(current, max_dp * current, min_dp * current)

            max_dp = new_max
            min_dp = new_min

            answer = max(new_max,answer)
        
        return answer 
        