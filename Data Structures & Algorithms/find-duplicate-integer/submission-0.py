class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #extra space 

        dups = set()
        for num in nums:
            if num in dups:
                return num 
            dups.add(num)
        return -1
        
        