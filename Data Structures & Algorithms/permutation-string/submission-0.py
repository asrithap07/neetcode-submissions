
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        counts = defaultdict(int)

        # Build the frequency map
        for letter in s1:
            counts[letter] += 1

        l = 0

        for r in range(len(s2)):

            # We are adding this character into the window
            counts[s2[r]] -= 1

            # If we now have too many of this character,
            # shrink the window from the left.
            while counts[s2[r]] < 0:
                counts[s2[l]] += 1
                l += 1

            # If the window is exactly the right size,
            # we found a permutation.
            if r - l + 1 == len(s1):
                return True

        return False
