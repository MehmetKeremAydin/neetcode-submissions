class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cheapestReach = [math.inf] * n
        cheapestReach[src] = 0
        for i in range(k+1):
            temp = cheapestReach.copy()
            for flight in flights:
                sorc, dest, prc = flight
                if cheapestReach[sorc] == math.inf:
                    continue
                temp[dest] = min(cheapestReach[sorc] + prc, temp[dest])
            cheapestReach = temp
        return -1 if cheapestReach[dst] == math.inf else cheapestReach[dst]
