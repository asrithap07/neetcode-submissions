class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            currentVal = nums[i]
            lookup = target - currentVal
            if lookup in seen.keys():
                return [seen[lookup], i]
            seen[currentVal] = i