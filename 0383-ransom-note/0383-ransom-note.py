class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # using counter class
        ransomNoteCounter = collections.Counter(ransomNote)
        magazineCounter = collections.Counter(magazine)

        # Iterate through the ransomeNote and check if the exact occurence of characters are there or not.

        for char in ransomNote:
            if (char not in magazineCounter) or (ransomNoteCounter.get(char) > magazineCounter.get(char)):
                return False
        return True

        