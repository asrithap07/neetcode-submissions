class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                print(s[l] + "is not alnum")
                l += 1
            if not s[r].isalnum():
                print(s[r] + "is not alnum")
                r -= 1
            if s[l].lower() == s[r].lower():
                print(s[l] + " " + s[r] + " are equal")
                l += 1
                r -= 1
            elif s[l].lower() != s[r].lower() and (s[l].isalnum() and s[r].isalnum()):
                print(s[l] + " " + s[r] + " are not equal")
                return False
        return True