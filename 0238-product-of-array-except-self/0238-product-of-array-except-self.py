class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sizeOfGivenArray = len(nums)

        res = [1] * sizeOfGivenArray

        # Calculate prefix
        for i in range(1, sizeOfGivenArray):
            res[i] = res[i - 1] * nums[i - 1]
        
        # Calculate postfix
        postfix = 1

        for j in range(sizeOfGivenArray - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res