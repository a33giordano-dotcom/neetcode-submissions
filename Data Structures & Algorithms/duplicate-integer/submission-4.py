class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbersset = set()

        for num in nums:
            if num in numbersset:
                return True 
            numbersset.add(num)
        
        return False 

        
        