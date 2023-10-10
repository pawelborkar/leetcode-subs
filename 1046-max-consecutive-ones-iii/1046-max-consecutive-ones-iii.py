class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        res = 0
        zero_counts = 0
        while right < len(nums):
            # Check for 0 and increment the zero_counts
            if nums[right] == 0:
                zero_counts += 1
            
            # If the zero_countes exceeds the k then we have remove the elements from the back
            while zero_counts > k:
                # remove the elements at left which are zero and decrement the zero count and move left pointer forward
                if nums[left] == 0:
                    zero_counts -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
