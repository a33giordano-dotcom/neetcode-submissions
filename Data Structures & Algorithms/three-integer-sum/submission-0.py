class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue 

            b, c = i + 1, len(nums)-1

            while b < c:
                three_sum = a + nums[b] + nums[c]

                if three_sum > 0:
                    c -= 1
                elif three_sum < 0:
                    b += 1
                else:
                    res.append([a, nums[b], nums[c]])
                    b += 1
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1
        return res