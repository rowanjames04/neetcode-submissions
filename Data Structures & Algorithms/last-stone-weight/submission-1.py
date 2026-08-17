class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            # this is greater than instead of less than because the 
            # heap has negatives to make it a maxheap
            if second < first:
                heapq.heappush(stones, -1 * (first - second))

        stones.append(0)
        return abs(stones[0])
