class Solution:
    import heapq

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)
        maxHeap = []
        res = []

        #loop through each value in nums
        for num in nums:
            #store counts in a dictionary
            counts[num] += 1
        
        #loop through the hashmap
        for key in counts:
            #store (count, val) into a maxHeap
            heapq.heappush(maxHeap, (-(counts[key]), key))

        #append top k values -> tuple[1] to the returning array
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        
        #return result
        return res

        