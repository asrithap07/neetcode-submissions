class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = {}
        right = {}
        for i in range(len(nums)):
            left[i] = nums[i] * left.get(i-1, 1)
            right[len(nums) - 1 - i] = nums[len(nums) - 1 - i] * right.get(len(nums) - i, 1)
        
        print(left)
        print(right)
        for i in range(len(nums)):
            output.append(left.get(i - 1, 1) * right.get(i + 1, 1))
        
        return output