class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i, num in enumerate(nums):
            
            # Check if it's duplicate
            if nums[abs(num)] < 0:
                return abs(num)
            
            nums[abs(num)] *= -1
      