class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

            # Check for nullables
            if len(nums) == 0:
                return 0
            # if len(nums) == 1:
            #     return 1

            longest_seq = 1
            nums_set = set(nums)

            for i, num in enumerate(nums):
                # Check if the current element is a starting element in the sequence
                if i >= 0 and num - 1 not in nums_set:
                    count = 1

                    # Check for num + 1 in nums_set and if found increase the count
                    while num + count in nums_set:
                        count += 1

                    longest_seq = max(longest_seq, count)
            return longest_seq




