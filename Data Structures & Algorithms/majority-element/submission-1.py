class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        maxx = 0
        res = 0 
        for key, value in counter.items():
            if value > maxx:
                maxx = value
                res = key 
            
        return res 

        