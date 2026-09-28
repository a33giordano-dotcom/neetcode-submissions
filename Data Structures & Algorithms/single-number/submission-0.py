class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = Counter(nums)

        for key, val in s.items():
            if val < 2:
                return key
        
        