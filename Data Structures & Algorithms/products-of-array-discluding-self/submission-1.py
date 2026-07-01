class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = {0:nums[0]}
        right = {(len(nums) - 1): nums[(len(nums) - 1)]} 
        res = [0] * len(nums)

        #loop from left to right
        for i in range(1, len(nums)):
            #for each index put it in the left hashmap with the prpoduict of iall the numbers before it
            left[i] = left[i - 1] * nums[i]
        
        #vice versa with right to left
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i]

        #create the new array using these values
        for i in range(len(nums)):
            if i == 0:
                res[i] = right[i + 1]
            elif i == (len(nums) - 1):
                res[i] = left[i - 1]
            else:
                res[i] = left[i - 1] * right[i + 1]
        
        return res
