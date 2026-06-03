class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = {}
        for letter in s:
            tracker[letter] = tracker.get(letter, 0) + 1
        for letter in t:
            if letter in tracker:
                tracker[letter] = tracker[letter] - 1
            else:
                return False
        return all(v == 0 for v in tracker.values() )