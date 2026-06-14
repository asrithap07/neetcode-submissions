import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxStreak = 0
        for num in seen:
            if (num - 1) not in seen:
                currStreak = 1
                while (num + 1) in seen:
                    currStreak += 1
                    num = num + 1
                maxStreak = max(currStreak, maxStreak)
        return maxStreak
