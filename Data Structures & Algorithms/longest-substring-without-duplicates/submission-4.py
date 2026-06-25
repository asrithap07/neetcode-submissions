class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        l,r = 0, 1
        longest = 0
        curr = {s[0]}

        while r < len(s):
            if s[r] not in curr:
                curr.add(s[r])
                longest = max(longest, len(curr))
                r += 1
            else:
                curr.remove(s[l])
                l += 1
        return longest
            
        