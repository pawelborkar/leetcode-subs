class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Check if the lengths are equal
        if len(s) != len(t):
            return False
        
        # Counts the occurence of each character in the given strings
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        
        # Checks for exact occurences of a character in both the strings
        for i, char in enumerate(s):
            if counter_s.get(char) != counter_t.get(char):
                return False
        return True
