class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Using 2-pointers
        res = []
        print(res)
        left, right = 0, len(nums) - 1

        while left <= right:
            leftSquare = nums[left] * nums[left]
            rightSquare = nums[right] * nums[right]

            if leftSquare >= rightSquare:
                res.append(leftSquare)
                left += 1
            else:
                res.append(rightSquare)
                right -= 1
        return res[::-1]
