class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost2reach = [math.inf] * n
        temp = [math.inf] * n
        cost2reach[src],temp[src] = 0, 0
        for i in range(k+1):
            for f in flights:
                if cost2reach[f[0]] != math.inf and cost2reach[f[0]] + f[2] <= temp[f[1]]: 
                    temp[f[1]] = cost2reach[f[0]] + f[2]
                    #print("TOOK:", f, temp)
                    #print("SKIP:", f, temp)
            cost2reach = list(temp)
            #print(cost2reach)
        return -1 if cost2reach[dst] == math.inf else cost2reach[dst]