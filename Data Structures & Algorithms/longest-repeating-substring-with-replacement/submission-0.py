class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0, 0
        tracker = {}
        longestSubstring = 0
        while r < len(s):
            tracker[s[r]] = tracker.get(s[r], 0) + 1
            #this part is O(n)
            windowLength = r - l + 1
            currValsToReplace = windowLength - max(tracker.values())
            print(currValsToReplace)
            if currValsToReplace > k:
                tracker[s[l]] -= 1
                l += 1
            else:
                curr = windowLength
                longestSubstring = max(curr, longestSubstring)
            r += 1
        return longestSubstring
