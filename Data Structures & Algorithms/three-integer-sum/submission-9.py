class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []
        #loop through each number
        for i in range(len(nums) - 1):
            #if its a number we've seen before, we should skip it
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            #create left and right opp-end pointers that start after the current number
            l, r = i + 1, len(nums) - 1 #this could cause index out of bounds
            #loop
            while l < r:
                #do 2sum with those numbers
                sum = nums[i] + nums[l] + nums[r]
                #adjust pointers accordingly based on if scenarios
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                #if theres a result check it again the current list and then add it
                    triplet = [nums[i], nums[l], nums[r]]
                    if triplet not in res:
                        res.append(triplet)
                    l += 1
        #return the result
        return res