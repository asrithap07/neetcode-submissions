class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        count = 0
        while count < (len(s) // 2):
            if s[left].isalnum() and (not s[right].isalnum()):
                right -= 1
            if (not s[left].isalnum()) and s[right].isalnum():
                left += 1
            if (not s[left].isalnum()) or (not s[right].isalnum()): 
                count += 1
                continue

            if s[left].lower() != s[right].lower():
                    return False
            else:
                left += 1
                right -= 1
            count += 1
        return True