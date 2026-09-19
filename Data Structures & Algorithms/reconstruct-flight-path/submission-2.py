class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        route = []

        def visit(airport):
            while adj[airport]:
                next_dest = heapq.heappop(adj[airport])
                visit(next_dest)
            route.append(airport)

        visit("JFK")
        return route[::-1]