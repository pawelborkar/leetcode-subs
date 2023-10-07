class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        longest_consecutive_seq = 0

        num_set = set(nums) #Converting to hash set in order to achieve O(1) TC while accessing

        for num in nums:
        # Check if the current num is the start of the sequence
            if num - 1 not in num_set:
                current_length = 1

                while num + current_length in num_set:
                    current_length += 1
            
                longest_consecutive_seq = max(longest_consecutive_seq, current_length)
        return longest_consecutive_seq


