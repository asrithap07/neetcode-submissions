import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        maxHeap = []
        for num in nums:
            if num in tracker:
                tracker[num]+=1
            else:
                tracker[num] = 1
        for key in tracker:
            heapq.heappush(maxHeap, (-(tracker[key]), key))
        ret = []
        for i in range(k):
            maxVal = (heapq.heappop(maxHeap))[1]
            ret.append(maxVal)
        return ret