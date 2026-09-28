class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapper = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in mapper:
                return[mapper[diff], i+1]
            mapper[n] = i + 1
        return -1