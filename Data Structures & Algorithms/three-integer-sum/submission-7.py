class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums)):
            num = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            newTarget = 0 - num
            l,r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum < newTarget:
                    l += 1
                elif sum > newTarget:
                    r -= 1
                else:
                    ret.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ret
