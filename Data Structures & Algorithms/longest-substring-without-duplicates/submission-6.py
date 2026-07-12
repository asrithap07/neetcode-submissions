class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0
        seen = set()
        #while r hasnt reached the end of the string
        while r < len(s):
            #if the righter pointer letter is already in the set
            while s[r] in seen:
                #remove that left value from seen -> we need to "reset" our. substring
                seen.remove(s[l])
                #move the left pointer
                l += 1
            #add the current letter to the set
            seen.add(s[r])
            #save longest lenth
            longest = max(longest, len(seen))
            #increment right pointer by 1
            r += 1
        return longest