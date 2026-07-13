class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l, r = 0, 0
        longest = 0

        #loop through the string to do replacesments
        while r < len(s):
            counts[s[r]] += 1
            #if the window is invalid
            while (r - l + 1) - max(counts.values()) > k:
                #shrink left until its valid
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
            r += 1
        return longest
