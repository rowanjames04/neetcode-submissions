class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = []
        for n in nums:
            neg.append(-1 * n)
        
        heapq.heapify(neg)

        while k > 0:
            res = heapq.heappop(neg)
            k -= 1
        
        return res * -1