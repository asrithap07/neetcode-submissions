class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums) > pow(10,5)):
            return False;
        seenNums = [];
        for i in range(len(nums)):
            if nums[i] in seenNums:
                return True;
            seenNums.append(nums[i])
        return False;