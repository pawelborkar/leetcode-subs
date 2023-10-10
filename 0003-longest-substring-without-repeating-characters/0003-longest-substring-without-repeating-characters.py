class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Using set
        left = 0
        max_length = 0
        char_set = set()

        for right, char in enumerate(s):

            if char not in char_set:
                char_set.add(char)
                max_length = max(max_length, right - left + 1)
            else:
                while char in char_set:
                    char_set.remove(s[left])  # move the window forward by removing the extra char from the left
                    left += 1
                char_set.add(char)
        return max_length

