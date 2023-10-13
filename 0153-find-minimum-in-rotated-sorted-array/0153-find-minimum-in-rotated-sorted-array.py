class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Base cases
        # If length of nums is 1
        size_of_given_array = len(nums)

        if size_of_given_array == 1:
            return nums[0]
        
        # If the first element is smaller than the last element then the array has 0 rotation
        if nums[0] < nums[size_of_given_array - 1]:
            return nums[0]
        
        left, right = 0, size_of_given_array - 1

        while left <= right:
            mid = (left + right) // 2

            # if the mid element is greater than it's adjacent element on the right then the adjacent element is the inflection point i.e. the smallest element in the given array
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            # Otherwise shrink the search space

            # Left sorted array
            if nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
