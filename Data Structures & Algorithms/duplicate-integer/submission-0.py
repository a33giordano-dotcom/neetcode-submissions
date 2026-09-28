from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper = {}
        for num in nums:
            if num not in mapper:
                mapper[num] = 1
            else:
                mapper[num] += 1
                if mapper[num] >= 2:
                    return True 
        return False
         