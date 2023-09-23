class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)

        # Check if the lengths are equal
        if len(s) != len(t):
            return False
        
        # If equal then count the occurence of each character using counter

        for i, char in enumerate(s):
            if counter_s.get(char) != counter_t.get(char):
                return False
        return True
