class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = k = l = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                k += 1
            res = max(res, k)
            if nums[i] == 0:
                k = 0
        return res