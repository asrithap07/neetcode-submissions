import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        heapq.heapify(nums)
        prev = heapq.heappop(nums)

        current_streak = 1
        best_streak = 1

        while nums:
            curr = heapq.heappop(nums)

            if curr == prev:
                pass

            elif curr == prev + 1:
                current_streak += 1
                best_streak = max(best_streak, current_streak)

            else:
                current_streak = 1

            prev = curr

        return best_streak