class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        left = 0
        count = 0
        for right, num in enumerate(nums):
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                # Restart the count 
                count = 0
                left = right 
        return res
