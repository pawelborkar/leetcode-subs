class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        We have to perform two steps and that are
        1. Convert all chars to lower case and remove all spaces and special chars
        2. Check if the new string is a palindrome or not
        '''
        new_string = ""
        for char in s:
            if char.isalnum():
                new_string += char.lower()
        
        #Check if the new string is a palindrome

        left, right = 0, len(new_string) - 1

        while left <= right:
            if new_string[left] != new_string[right]:
                return False
            left += 1
            right -= 1
        return True
      