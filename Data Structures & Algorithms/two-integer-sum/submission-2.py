class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in mapper:
                return [mapper[difference], i]
            mapper[num] = i
        
        return 0
        