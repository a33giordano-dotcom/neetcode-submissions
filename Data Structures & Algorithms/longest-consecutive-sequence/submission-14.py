class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = set(nums)
        long = 0

        for num in nums:
            if num - 1 not in longest:
                leng = 1
                while (num + leng) in longest:
                    leng += 1
            
                long = max(long, leng)
        
        return long
