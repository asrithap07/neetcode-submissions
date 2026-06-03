class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = set();
        for i in range(len(nums)):
            if nums[i] in seenNums:
                return True;
            seenNums.add(nums[i])
        return False;