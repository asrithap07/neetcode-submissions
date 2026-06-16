class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            temp = numbers[l] + numbers[r]
            if temp < target:
                l += 1
                print(l)
            if temp > target:
                r -= 1
                print(r)
            if temp == target:
                return [l + 1, r + 1]
