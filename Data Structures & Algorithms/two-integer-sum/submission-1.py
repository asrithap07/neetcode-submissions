class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i in range(len(nums)):
            searchVal = target - nums[i]
            if searchVal in seen:
                return [seen[searchVal], i]
            else:
                seen[nums[i]] = i